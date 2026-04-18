"""Auto-generated tool stubs from FortiEDR Postman collection.

THIS FILE IS AUTO-GENERATED — DO NOT EDIT BY HAND.
To regenerate: python tools/gen_tools.py

Category: management-rest/audit
Endpoint count: 1
"""
from __future__ import annotations

from typing import Any

from mcp.server.fastmcp import FastMCP

from ...auth import AuthManager
from ...client import FortiEDRClient



def register_read(mcp: FastMCP, auth: AuthManager) -> None:
    @mcp.tool(name="audit_get_audit")
    async def audit_get_audit(
        organization: str | None = None,
        fromTime: str | None = None,
        toTime: str | None = None,
    ) -> Any:
        """This API retrieve the audit between 2 dates
        
        Endpoint: `GET /management-rest/audit/get-audit`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            fromTime: Retrieves audit that were written after the given date. Date Format: yyyy-MM-dd (Default is current date)
            toTime: Retrieves audit that were written before the given date. Date Format: yyyy-MM-dd (Default is current date)
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
            "/management-rest/audit/get-audit",
            params={
            "fromTime": fromTime,
            "toTime": toTime
        },
            organization=organization,
        )

