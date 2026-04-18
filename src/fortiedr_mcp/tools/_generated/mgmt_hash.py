"""Auto-generated tool stubs from FortiEDR Postman collection.

THIS FILE IS AUTO-GENERATED — DO NOT EDIT BY HAND.
To regenerate: python tools/gen_tools.py

Category: management-rest/hash
Endpoint count: 1
"""
from __future__ import annotations

from typing import Any

from mcp.server.fastmcp import FastMCP

from ...auth import AuthManager
from ...client import FortiEDRClient



def register_read(mcp: FastMCP, auth: AuthManager) -> None:
    @mcp.tool(name="hash_search")
    async def hash_search(
        organization: str | None = None,
        fileHashes: str | None = None,
    ) -> Any:
        """This API enables the user to search a file hash among the current events, threat hunting repository and communicating applications that exist in the system
        
        Endpoint: `GET /management-rest/hash/search`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            fileHashes: (Required) Specifies the list of files hashes
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
            "/management-rest/hash/search",
            params={
            "fileHashes": fileHashes
        },
            organization=organization,
        )

