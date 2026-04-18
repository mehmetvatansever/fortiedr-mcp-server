"""Auto-generated tool stubs from FortiEDR Postman collection.

THIS FILE IS AUTO-GENERATED — DO NOT EDIT BY HAND.
To regenerate: python tools/gen_tools.py

Category: api/dashboard
Endpoint count: 2
"""
from __future__ import annotations

from typing import Any

from mcp.server.fastmcp import FastMCP

from ...auth import AuthManager
from ...client import FortiEDRClient



def register_read(mcp: FastMCP, auth: AuthManager) -> None:
    @mcp.tool(name="dashboard_most_targeted_items")
    async def dashboard_most_targeted_items(
        organization: str | None = None,
        itemType: str | None = None,
        numOfColumns: int | None = None,
        numOfDays: int | None = None,
    ) -> Any:
        """Returns most targeted devices or most targeted processes, depending on the itemType parameter
        
        Endpoint: `GET /api/dashboard/most-targeted-items`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            itemType: Specifies the type of items
            numOfColumns: Specifies the number of columns to present
            numOfDays: Specifies the number of days to present
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
            "/api/dashboard/most-targeted-items",
            params={
            "itemType": itemType,
            "numOfColumns": numOfColumns,
            "numOfDays": numOfDays
        },
            organization=organization,
        )

    @mcp.tool(name="dashboard_unhandled_items")
    async def dashboard_unhandled_items(
        organization: str | None = None,
        itemType: str | None = None,
    ) -> Any:
        """Returns unhandled devices or unhandled processes, depending on the itemType parameter
        
        Endpoint: `GET /api/dashboard/unhandled-items`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            itemType: Specifies the type of items
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
            "/api/dashboard/unhandled-items",
            params={
            "itemType": itemType
        },
            organization=organization,
        )

