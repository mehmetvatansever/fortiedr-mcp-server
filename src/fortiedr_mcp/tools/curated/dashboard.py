"""Curated dashboard tools.

Fixes the optional parameters in the auto-generated version — the
itemType, numOfColumns and numOfDays fields that FortiEDR requires are
exposed with sensible defaults.
"""
from __future__ import annotations

from typing import Any

from mcp.server.fastmcp import FastMCP

from ...auth import AuthManager
from ...client import FortiEDRClient

OVERRIDES = {
    "dashboard_unhandled_items",
    "dashboard_most_targeted_items",
}


def register_read(mcp: FastMCP, auth: AuthManager) -> None:
    @mcp.tool(name="dashboard_unhandled_items")
    async def dashboard_unhandled_items(
        organization: str | None = None,
        item_type: str = "device",
    ) -> Any:
        """Return the unhandled items shown on the dashboard.

        Args:
            organization: Target tenant. Defaults to the default org.
            item_type: 'device' or 'process'. Default: device.
        """
        org = auth.resolve_org(organization)
        async with _client(auth) as c:
            return await c.get(
                "/api/dashboard/unhandled-items",
                params={"itemType": item_type, "organization": org},
            )

    @mcp.tool(name="dashboard_most_targeted_items")
    async def dashboard_most_targeted_items(
        organization: str | None = None,
        item_type: str = "device",
        num_of_columns: int = 10,
        num_of_days: int = 30,
    ) -> Any:
        """Return the most-targeted devices or processes over the last N days.

        Ideal for monthly reports or a dashboard visualisation.

        Args:
            organization: Target tenant.
            item_type: 'device' or 'process'.
            num_of_columns: How many rows to return (default 10).
            num_of_days: How many days to look back (default 30).
        """
        org = auth.resolve_org(organization)
        async with _client(auth) as c:
            return await c.get(
                "/api/dashboard/most-targeted-items",
                params={
                    "itemType": item_type,
                    "numOfColumns": num_of_columns,
                    "numOfDays": num_of_days,
                    "organization": org,
                },
            )


def _client(auth: AuthManager) -> FortiEDRClient:
    cfg = auth.config
    return FortiEDRClient(
        host=cfg.host, user=cfg.user, password=cfg.password,
        default_org=cfg.default_org, verify_ssl=cfg.verify_ssl,
    )
