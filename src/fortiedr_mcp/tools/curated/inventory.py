"""Curated inventory (collector) tools.

Adds safety checks and explicit docstring warnings for destructive
actions (isolate/unisolate/delete).
"""
from __future__ import annotations

from typing import Any

from mcp.server.fastmcp import FastMCP

from ...auth import AuthManager
from ...client import FortiEDRClient

OVERRIDES = {
    "inventory_list_collectors",
    "inventory_isolate_collectors",
    "inventory_unisolate_collectors",
}


def register_read(mcp: FastMCP, auth: AuthManager) -> None:
    @mcp.tool(name="inventory_list_collectors")
    async def inventory_list_collectors(
        organization: str | None = None,
        group_name: str | None = None,
        os_family: str | None = None,
        state: str | None = None,
        device_name: str | None = None,
        ip: str | None = None,
        logged_user: str | None = None,
        version: str | None = None,
    ) -> Any:
        """List FortiEDR collectors (endpoint agents) with filters.

        Valid values:
        - os_family: Windows, macOS, Linux
        - state: Running, Disconnected, Isolated, Disabled, Degraded, Pending

        Args:
            organization: Target tenant (MSSP).
            group_name: Collector group.
            os_family: Operating system family.
            state: Collector state.
            device_name: Device name (partial match).
            ip: IP address.
            logged_user: Currently logged-on user.
            version: Collector version.
        """
        params = {
            "groupName": group_name,
            "osFamily": os_family,
            "state": state,
            "device": device_name,
            "ip": ip,
            "loggedUser": logged_user,
            "version": version,
        }
        async with _client(auth) as c:
            return await c.get(
                "/management-rest/inventory/list-collectors",
                params=params,
                organization=auth.resolve_org(organization),
            )


def register_destructive(mcp: FastMCP, auth: AuthManager) -> None:
    @mcp.tool(name="inventory_isolate_collectors")
    async def inventory_isolate_collectors(
        device_names: list[str],
        organization: str | None = None,
        reason: str | None = None,
    ) -> Any:
        """DESTRUCTIVE: Isolate one or more endpoints from the network.

        THIS OPERATION:
        - Cuts the endpoint off the network (only FortiEDR management traffic remains)
        - Causes business disruption
        - Requires user notification and approval

        In MSSP environments: logging which customer's device was isolated
        to the AUDIT LOG IS MANDATORY. Fill in the reason parameter.

        Args:
            device_names: Full names of the devices to isolate.
            organization: Target tenant (MSSP) — picking the wrong org is disastrous!
            reason: Reason for isolation (ticket number, analyst note, etc.).
        """
        body: dict[str, Any] = {"devicesNames": device_names}
        if reason:
            body["reason"] = reason
        async with _client(auth) as c:
            return await c.put(
                "/management-rest/inventory/isolate-collectors",
                json_body=body,
                organization=auth.resolve_org(organization),
            )

    @mcp.tool(name="inventory_unisolate_collectors")
    async def inventory_unisolate_collectors(
        device_names: list[str],
        organization: str | None = None,
    ) -> Any:
        """Remove isolation from previously isolated endpoints.

        Un-isolation is also considered destructive because the endpoint
        re-joins the network.
        """
        async with _client(auth) as c:
            return await c.put(
                "/management-rest/inventory/unisolate-collectors",
                json_body={"devicesNames": device_names},
                organization=auth.resolve_org(organization),
            )


def _client(auth: AuthManager) -> FortiEDRClient:
    cfg = auth.config
    return FortiEDRClient(
        host=cfg.host, user=cfg.user, password=cfg.password,
        default_org=cfg.default_org, verify_ssl=cfg.verify_ssl,
    )
