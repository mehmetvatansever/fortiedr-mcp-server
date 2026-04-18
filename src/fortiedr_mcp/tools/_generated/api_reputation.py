"""Auto-generated tool stubs from FortiEDR Postman collection.

THIS FILE IS AUTO-GENERATED — DO NOT EDIT BY HAND.
To regenerate: python tools/gen_tools.py

Category: api/reputation
Endpoint count: 2
"""
from __future__ import annotations

from typing import Any

from mcp.server.fastmcp import FastMCP

from ...auth import AuthManager
from ...client import FortiEDRClient



def register_read(mcp: FastMCP, auth: AuthManager) -> None:
    @mcp.tool(name="reputation_regions")
    async def reputation_regions(
        organization: str | None = None,
        organizationId: int | None = None,
    ) -> Any:
        """retrieves reputation region entity
        
        Endpoint: `GET /api/reputation/regions`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            organizationId: (Required) organizationId
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
            "/api/reputation/regions",
            params={
            "organizationId": organizationId
        },
            organization=organization,
        )


def register_write(mcp: FastMCP, auth: AuthManager) -> None:
    @mcp.tool(name="reputation_regions")
    async def reputation_regions(
        organization: str | None = None,
        organizationId: int | None = None,
        body: list[Any] | None = None,
    ) -> Any:
        """select regions for specific organization
        
        Endpoint: `PUT /api/reputation/regions`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            organizationId: (Required) organizationId
            body: Request body (JSON array).
        """
        auth.ensure(organization)
        async with FortiEDRClient(
            host=auth.config.host,
            user=auth.config.user,
            password=auth.config.password,
            default_org=auth.config.default_org,
            verify_ssl=auth.config.verify_ssl,
        ) as client:
            return await client.put(
            "/api/reputation/regions",
            params={
            "organizationId": organizationId
        },
            json_body=body,
            organization=organization,
        )

