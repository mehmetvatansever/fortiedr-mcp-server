"""Tool registry — loads generated, curated, and composite layers.

Load order matters: generated first, then curated, then composite.
Curated and composite modules can override same-named tools from the
generated layer via their OVERRIDES set.
"""
from __future__ import annotations

import importlib
import logging
import pkgutil
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mcp.server.fastmcp import FastMCP

    from ..auth import AuthManager

log = logging.getLogger(__name__)


def _load_submodules(package_name: str) -> list:
    """Import every module in a package and return them as a list."""
    package = importlib.import_module(package_name)
    modules = []
    for _, mod_name, _ in pkgutil.iter_modules(package.__path__):
        if mod_name.startswith("_") and mod_name != "__init__":
            continue
        full_name = f"{package_name}.{mod_name}"
        try:
            modules.append(importlib.import_module(full_name))
        except Exception as e:
            log.warning("Failed to load module %s: %s", full_name, e)
    return modules


def register_all(
    mcp: "FastMCP",
    auth: "AuthManager",
    *,
    read_only: bool,
    enable_destructive: bool,
    expose_raw_api: bool = False,
) -> int:
    """Load every layer. Returns the number of registered tools.

    Load order: generated → curated → composite.
    Curated/composite modules can override tool names from the generated
    layer via their OVERRIDES attribute (blocking same-named registrations).

    When expose_raw_api is False (default), the generated layer is skipped
    entirely. This keeps the tool surface focused on the curated and
    composite tools that real MDR workflows use, which makes Claude's
    tool selection much more reliable.
    """
    overridden: set[str] = set()

    # 1) Discover curated and composite modules first, collect override lists
    curated_modules = _load_submodules("fortiedr_mcp.tools.curated")
    composite_modules = _load_submodules("fortiedr_mcp.tools.composite")

    for mod in curated_modules + composite_modules:
        overrides = getattr(mod, "OVERRIDES", ()) or ()
        for name in overrides:
            overridden.add(name)

    count = 0

    # 2) Generated modules — only register when raw API exposure is enabled
    if expose_raw_api:
        generated_modules = _load_submodules("fortiedr_mcp.tools._generated")
        for mod in generated_modules:
            count += _register_module(mod, mcp, auth, read_only, enable_destructive, skip=overridden)
    else:
        log.info("Skipping %d _generated modules (set FORTIEDR_EXPOSE_RAW_API=true to enable)",
                 len(list(_iter_submodule_names("fortiedr_mcp.tools._generated"))))

    # 3) Curated modules
    for mod in curated_modules:
        count += _register_module(mod, mcp, auth, read_only, enable_destructive)

    # 4) Composite modules
    for mod in composite_modules:
        count += _register_module(mod, mcp, auth, read_only, enable_destructive)

    log.info(
        "Tool registration complete: %d tools (overridden: %d, raw_api=%s)",
        count, len(overridden), expose_raw_api,
    )
    return count


def _iter_submodule_names(package_name: str):
    try:
        package = importlib.import_module(package_name)
    except Exception:
        return
    for _, mod_name, _ in pkgutil.iter_modules(package.__path__):
        if mod_name.startswith("_") and mod_name != "__init__":
            continue
        yield mod_name


def _register_module(
    mod,
    mcp: "FastMCP",
    auth: "AuthManager",
    read_only: bool,
    enable_destructive: bool,
    skip: set[str] | None = None,
) -> int:
    """Invoke the module's matching register_X functions."""
    skip = skip or set()
    count = 0

    # Proxy: wrap FastMCP and filter out names in the skip set
    class _FilteredMCP:
        def __init__(self, real_mcp):
            self._real = real_mcp

        def tool(self, *args, **kwargs):
            name = kwargs.get("name")

            def decorator(fn):
                nonlocal count
                tool_name = name or fn.__name__
                if tool_name in skip:
                    log.debug("Skipping %s (overridden)", tool_name)
                    return fn
                count += 1
                return self._real.tool(*args, **kwargs)(fn)
            return decorator

    proxy = _FilteredMCP(mcp)

    # Read is always loaded
    if hasattr(mod, "register_read"):
        try:
            mod.register_read(proxy, auth)
        except Exception as e:
            log.warning("register_read failed in %s: %s", mod.__name__, e)

    if not read_only and hasattr(mod, "register_write"):
        try:
            mod.register_write(proxy, auth)
        except Exception as e:
            log.warning("register_write failed in %s: %s", mod.__name__, e)

    if not read_only and enable_destructive and hasattr(mod, "register_destructive"):
        try:
            mod.register_destructive(proxy, auth)
        except Exception as e:
            log.warning("register_destructive failed in %s: %s", mod.__name__, e)

    return count
