"""Auto-generated tool stubs from FortiEDR Postman collection.

THIS FILE IS AUTO-GENERATED — DO NOT EDIT BY HAND.
To regenerate: python tools/gen_tools.py

Category: api/admin
Endpoint count: 2
"""
from __future__ import annotations

from typing import Any

from mcp.server.fastmcp import FastMCP

from ...auth import AuthManager
from ...client import FortiEDRClient



def register_write(mcp: FastMCP, auth: AuthManager) -> None:
    @mcp.tool(name="admin_set_enable_default_application_control_state")
    async def admin_set_enable_default_application_control_state(
        organization: str | None = None,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Update default application control state
        
        Endpoint: `PUT /api/admin/set-enable-default-application-control-state`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            body: Request body (JSON). Expected fields: isEnableDefaultApplicationControl, organization.
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
            "/api/admin/set-enable-default-application-control-state",
            params=None,
            json_body=body,
            organization=organization,
        )

    @mcp.tool(name="admin_set_tray_notification_settings")
    async def admin_set_tray_notification_settings(
        organization: str | None = None,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Update tray notification settings
        
        Endpoint: `POST /api/admin/set-tray-notification-settings`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            body: Request body (JSON). Expected fields: enabledPopup, enabledTrayNotification, message, organization, enableFortiClientNotification, showNotificationOnFileReadAttempt.
        """
        auth.ensure(organization)
        async with FortiEDRClient(
            host=auth.config.host,
            user=auth.config.user,
            password=auth.config.password,
            default_org=auth.config.default_org,
            verify_ssl=auth.config.verify_ssl,
        ) as client:
            return await client.post(
            "/api/admin/set-tray-notification-settings",
            params=None,
            json_body=body,
            organization=organization,
        )

