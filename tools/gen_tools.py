"""Generate MCP tool stubs from the Postman collection.

For each endpoint, emits an `@mcp.tool()` function into
`src/fortiedr_mcp/tools/_generated/<category>.py`.

The generated code MUST NOT be edited by hand — it gets overwritten on
re-run. Keep manual, polished versions under
`src/fortiedr_mcp/tools/<category>.py` instead.

Usage:
    python tools/gen_tools.py \
        fortiedr_api.postman_collection.json \
        src/fortiedr_mcp/tools/_generated
"""
from __future__ import annotations

import re
import sys
from collections import defaultdict
from pathlib import Path
from textwrap import indent

# Sibling module in the same directory
sys.path.insert(0, str(Path(__file__).parent))
from postman_parser import Endpoint, load_endpoints  # noqa: E402

HEADER = '''"""Auto-generated tool stubs from FortiEDR Postman collection.

THIS FILE IS AUTO-GENERATED — DO NOT EDIT BY HAND.
To regenerate: python tools/gen_tools.py

Category: {category}
Endpoint count: {count}
"""
from __future__ import annotations

from typing import Any

from mcp.server.fastmcp import FastMCP

from ...auth import AuthManager
from ...client import FortiEDRClient


'''

# Which HTTP method maps to which "category" in the FortiEDR API?
METHOD_CATEGORY = {
    "GET": "read",
    "POST": "write",    # some will be moved to destructive manually
    "PUT": "write",
    "DELETE": "destructive",
}

# Endpoints that are explicitly destructive (even if PUT/POST)
DESTRUCTIVE_PATTERNS = [
    "isolate", "unisolate", "uninstall", "delete", "remove",
    "toggle-collectors", "remediate", "release-license",
    "uninstall-collectors", "ems-move-collectors",
    "set-system-mode",
]


def classify(ep: Endpoint) -> str:
    """Classify an endpoint as read / write / destructive."""
    name_lower = ep.name.lower()
    path_lower = ep.path.lower()

    for pattern in DESTRUCTIVE_PATTERNS:
        if pattern in name_lower or pattern in path_lower:
            return "destructive"

    if ep.method == "DELETE":
        return "destructive"

    return METHOD_CATEGORY.get(ep.method, "read")


def param_type(value_hint: str) -> str:
    v = (value_hint or "").strip().lower()
    if v in ("true", "false"):
        return "bool"
    if v.isdigit() or (v.startswith("-") and v[1:].isdigit()):
        return "int"
    if v.replace(".", "", 1).isdigit():
        return "float"
    return "str"


def render_function(ep: Endpoint) -> str:
    """Emit Python tool-function code for a single endpoint."""

    fn_name = ep.python_fn_name
    action = classify(ep)

    # Parameter list
    params: list[str] = ["organization: str | None = None"]
    param_docs: list[str] = [
        "organization: Target organization in an MSSP environment (optional)."
    ]

    # Path parameters (required)
    for pp in ep.path_params:
        params.insert(0, f"{pp}: str")  # required — no default
        param_docs.insert(0, f"{pp}: Path parameter (required).")

    # Query parameters (optional)
    query_kwargs: list[tuple[str, str]] = []
    seen_py_names: set[str] = set(["organization"])
    for pp in ep.path_params:
        seen_py_names.add(pp)
    for q in ep.query_params:
        key = q["key"]
        if not key:
            continue
        # Convert to a Python identifier: dots and other special chars → _
        py_name = re.sub(r"[^a-zA-Z0-9_]", "_", key.replace("-", "_"))
        # Prefix if starts with a digit
        if py_name and py_name[0].isdigit():
            py_name = "p_" + py_name
        # Skip duplicates
        if py_name in seen_py_names:
            continue
        seen_py_names.add(py_name)
        ptype = param_type(q.get("value", ""))
        params.append(f"{py_name}: {ptype} | None = None")
        desc = q.get("description") or f"Query param: `{key}`"
        param_docs.append(f"{py_name}: {desc}")
        query_kwargs.append((key, py_name))

    # Body parameters
    body_kwarg = None
    if ep.body_type in ("json", "raw") and ep.body_schema:
        # Emitting one parameter per body field yields very long functions.
        # Fall back to a single `body: dict[str, Any] | None = None` instead.
        params.append("body: dict[str, Any] | None = None")
        param_docs.append(
            f"body: Request body (JSON). Expected fields: "
            f"{', '.join(ep.body_schema.keys())}."
        )
        body_kwarg = "body"
    elif ep.body_type == "json_array":
        params.append("body: list[Any] | None = None")
        param_docs.append("body: Request body (JSON array).")
        body_kwarg = "body"
    elif ep.body_type in ("formdata", "urlencoded"):
        params.append("body: dict[str, Any] | None = None")
        param_docs.append(f"body: {ep.body_type} fields as a dict.")
        body_kwarg = "body"

    params_str = ",\n        ".join(params)

    # Path substitution
    path_expr = f'"{ep.path}"'
    for pp in ep.path_params:
        path_expr = path_expr.replace(f":{pp}", f"{{{pp}}}").replace(f"{{{pp}}}", f"{{{pp}}}")
        path_expr = f'f{path_expr}' if 'f"' not in path_expr else path_expr
        # Shortcut: always emit an f-string
    if ep.path_params:
        path_expr = f'f"{ep.path}"'
        for pp in ep.path_params:
            path_expr = path_expr.replace(f":{pp}", f"{{{pp}}}")

    # Query dict
    if query_kwargs:
        query_items = ",\n            ".join(f'"{k}": {v}' for k, v in query_kwargs)
        params_dict = f"{{\n            {query_items}\n        }}"
    else:
        params_dict = "None"

    # Method call
    method_lower = ep.method.lower()
    if method_lower in ("post", "put", "delete") and body_kwarg:
        call = (
            f'await client.{method_lower}(\n'
            f'            {path_expr},\n'
            f'            params={params_dict},\n'
            f'            json_body={body_kwarg},\n'
            f'            organization=organization,\n'
            f'        )'
        )
    elif method_lower in ("post", "put"):
        call = (
            f'await client.{method_lower}(\n'
            f'            {path_expr},\n'
            f'            params={params_dict},\n'
            f'            organization=organization,\n'
            f'        )'
        )
    elif method_lower == "delete":
        call = (
            f'await client.delete(\n'
            f'            {path_expr},\n'
            f'            params={params_dict},\n'
            f'            organization=organization,\n'
            f'        )'
        )
    else:  # GET
        call = (
            f'await client.get(\n'
            f'            {path_expr},\n'
            f'            params={params_dict},\n'
            f'            organization=organization,\n'
            f'        )'
        )

    # Docstring
    summary = ep.description.split("\n")[0][:200] if ep.description else f"{ep.method} {ep.path}"
    docstring_lines = [f'"""{summary}', ""]
    if ep.description and ep.description != summary:
        docstring_lines.append(ep.description[:500])
        docstring_lines.append("")
    docstring_lines.append(f"Endpoint: `{ep.method} {ep.path}`")
    docstring_lines.append("")
    docstring_lines.append("Args:")
    for d in param_docs:
        docstring_lines.append(f"    {d}")
    docstring_lines.append('"""')
    # 8-space indent (tool function inside the register_X function)
    docstring = "\n        ".join(docstring_lines)

    # Full function
    code = f'''    @mcp.tool(name="{fn_name}")
    async def {fn_name}(
        {params_str},
    ) -> Any:
        {docstring}
        auth.ensure(organization)
        async with FortiEDRClient(
            host=auth.config.host,
            user=auth.config.user,
            password=auth.config.password,
            default_org=auth.config.default_org,
            verify_ssl=auth.config.verify_ssl,
        ) as client:
            return {call}
'''
    return code


def render_module(category: str, endpoints: list[Endpoint]) -> str:
    # Group by action
    buckets: dict[str, list[Endpoint]] = defaultdict(list)
    for ep in endpoints:
        buckets[classify(ep)].append(ep)

    code = HEADER.format(category=category, count=len(endpoints))

    for action in ("read", "write", "destructive"):
        eps = buckets.get(action, [])
        if not eps:
            continue
        code += f"\ndef register_{action}(mcp: FastMCP, auth: AuthManager) -> None:\n"
        for ep in eps:
            code += render_function(ep) + "\n"
        if not eps:
            code += "    pass\n"

    return code


def slugify_category(category: str) -> str:
    """Turn a category name into a file-name slug."""
    s = category.replace("management-rest/", "mgmt_").replace("api/", "api_")
    s = s.replace("/", "_").replace("-", "_").replace(" ", "")
    return s


def main() -> None:
    if len(sys.argv) != 3:
        print("Usage: gen_tools.py <postman.json> <output_dir>", file=sys.stderr)
        sys.exit(1)

    src = Path(sys.argv[1])
    out_dir = Path(sys.argv[2])
    out_dir.mkdir(parents=True, exist_ok=True)

    endpoints = load_endpoints(src)

    # Group by category
    by_cat: dict[str, list[Endpoint]] = defaultdict(list)
    for ep in endpoints:
        by_cat[ep.full_category].append(ep)

    # __init__.py
    init_lines = ['"""Auto-generated tool modules."""', "", "from . import ("]
    module_names = []
    for category, eps in sorted(by_cat.items()):
        mod_name = slugify_category(category)
        module_names.append(mod_name)
        code = render_module(category, eps)
        (out_dir / f"{mod_name}.py").write_text(code)
    init_lines.extend(f"    {m}," for m in sorted(module_names))
    init_lines.append(")")
    init_lines.append("")
    init_lines.append("__all__ = [")
    init_lines.extend(f'    "{m}",' for m in sorted(module_names))
    init_lines.append("]")
    (out_dir / "__init__.py").write_text("\n".join(init_lines) + "\n")

    print(f"Done: {len(endpoints)} endpoints -> {len(module_names)} modules, {out_dir}")


if __name__ == "__main__":
    main()
