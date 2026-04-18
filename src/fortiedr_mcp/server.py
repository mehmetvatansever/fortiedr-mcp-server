"""FortiEDR MCP Server — entry point.

Run:
    # stdio (Claude Desktop, Cursor, VS Code, Claude Code)
    python -m fortiedr_mcp

    # HTTP (remote deployment, e.g. Docker)
    FORTIEDR_TRANSPORT=http python -m fortiedr_mcp
"""
from __future__ import annotations

import logging
import os
import sys

from mcp.server.fastmcp import FastMCP

from .auth import AuthManager
from .config import Config
from .tools import register_all


def _setup_logging() -> None:
    level = os.getenv("FORTIEDR_LOG_LEVEL", "INFO").upper()
    logging.basicConfig(
        level=level,
        stream=sys.stderr,  # stdio transport: critical not to pollute stdout
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    )


def build_server() -> FastMCP:
    _setup_logging()
    cfg = Config.from_env()
    auth = AuthManager(cfg)

    mcp = FastMCP("fortiedr")

    count = register_all(
        mcp,
        auth,
        read_only=cfg.read_only,
        enable_destructive=cfg.enable_destructive,
        expose_raw_api=cfg.expose_raw_api,
    )

    mode_desc = []
    if cfg.read_only:
        mode_desc.append("READ-ONLY")
    else:
        mode_desc.append("read+write")
        if cfg.enable_destructive:
            mode_desc.append("+destructive")
    if cfg.expose_raw_api:
        mode_desc.append("+raw-api")
    logging.getLogger(__name__).info(
        "FortiEDR MCP ready | host=%s | org=%s | mode=%s | %d tools",
        cfg.host, cfg.default_org or "(none)", " ".join(mode_desc), count,
    )
    return mcp


def main() -> None:
    mcp = build_server()
    transport = os.getenv("FORTIEDR_TRANSPORT", "stdio").lower()

    if transport == "http":
        port = int(os.getenv("FORTIEDR_HTTP_PORT", "3000"))
        host = os.getenv("FORTIEDR_HTTP_HOST", "127.0.0.1")
        mcp.settings.host = host
        mcp.settings.port = port
        mcp.run(transport="streamable-http")
    else:
        mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
