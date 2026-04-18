"""Auto-generated tool stubs from FortiEDR Postman collection.

THIS FILE IS AUTO-GENERATED — DO NOT EDIT BY HAND.
To regenerate: python tools/gen_tools.py

Category: api/av-scanner-file-controller
Endpoint count: 1
"""
from __future__ import annotations

from typing import Any

from mcp.server.fastmcp import FastMCP

from ...auth import AuthManager
from ...client import FortiEDRClient



def register_read(mcp: FastMCP, auth: AuthManager) -> None:
    @mcp.tool(name="av_scanner_file_controller_stream_av_scanner_file")
    async def av_scanner_file_controller_stream_av_scanner_file(
        organization: str | None = None,
        version: str | None = None,
    ) -> Any:
        """Streams a file from GCS directly to client
        
        Endpoint: `GET /api/av-scanner-file-controller/download`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            version: (Required) version
        """
        auth.ensure(organization)
        async with FortiEDRClient(
            host=auth.config.host,
            user=auth.config.user,
            password=auth.config.password,
            default_org=auth.config.default_org,
            verify_ssl=auth.config.verify_ssl,
        ) as client:
            return await client.get(
            "/api/av-scanner-file-controller/download",
            params={
            "version": version
        },
            organization=organization,
        )

