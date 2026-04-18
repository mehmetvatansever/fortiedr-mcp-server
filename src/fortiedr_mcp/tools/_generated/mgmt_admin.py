"""Auto-generated tool stubs from FortiEDR Postman collection.

THIS FILE IS AUTO-GENERATED — DO NOT EDIT BY HAND.
To regenerate: python tools/gen_tools.py

Category: management-rest/admin
Endpoint count: 10
"""
from __future__ import annotations

from typing import Any

from mcp.server.fastmcp import FastMCP

from ...auth import AuthManager
from ...client import FortiEDRClient



def register_read(mcp: FastMCP, auth: AuthManager) -> None:
    @mcp.tool(name="admin_list_collector_installers")
    async def admin_list_collector_installers(
        organization: str | None = None,
    ) -> Any:
        """This API call output the available collectors installers
        
        Endpoint: `GET /management-rest/admin/list-collector-installers`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
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
            "/management-rest/admin/list-collector-installers",
            params=None,
            organization=organization,
        )

    @mcp.tool(name="admin_list_system_summary")
    async def admin_list_system_summary(
        organization: str | None = None,
        addLicenseBlob: bool | None = None,
    ) -> Any:
        """Get System Summary
        
        Endpoint: `GET /management-rest/admin/list-system-summary`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            addLicenseBlob: Indicates whether to put license blob to response. By default addLicenseBlob is false
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
            "/management-rest/admin/list-system-summary",
            params={
            "addLicenseBlob": addLicenseBlob
        },
            organization=organization,
        )

    @mcp.tool(name="admin_previous_registration_passwords")
    async def admin_previous_registration_passwords(
        organization: str | None = None,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """This API retrieve previous registration passwords for given organization
        
        Endpoint: `GET /management-rest/admin/previous-registration-passwords`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            body: Request body (JSON). Expected fields: organization.
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
            "/management-rest/admin/previous-registration-passwords",
            params=None,
            organization=organization,
        )

    @mcp.tool(name="admin_ready")
    async def admin_ready(
        organization: str | None = None,
    ) -> Any:
        """Get System Readiness
        
        Endpoint: `GET /management-rest/admin/ready`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
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
            "/management-rest/admin/ready",
            params=None,
            organization=organization,
        )


def register_write(mcp: FastMCP, auth: AuthManager) -> None:
    @mcp.tool(name="admin_registration_password")
    async def admin_registration_password(
        organization: str | None = None,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """This API creates new registration password for given organization
        
        Endpoint: `POST /management-rest/admin/registration-password`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            body: Request body (JSON). Expected fields: organization, password.
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
            "/management-rest/admin/registration-password",
            params=None,
            json_body=body,
            organization=organization,
        )

    @mcp.tool(name="admin_update_collector_installer")
    async def admin_update_collector_installer(
        organization: str | None = None,
        collectorGroupIds: int | None = None,
        collectorGroups: str | None = None,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """This API update collectors target version for collector groups
        
        Endpoint: `POST /management-rest/admin/update-collector-installer`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            collectorGroupIds: Specifies the list of IDs of all the collector groups which should be updated.
            collectorGroups: Specifies the list of all the collector groups which should be updated.
            body: Request body (JSON). Expected fields: updateVersions.
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
            "/management-rest/admin/update-collector-installer",
            params={
            "collectorGroupIds": collectorGroupIds,
            "collectorGroups": collectorGroups
        },
            json_body=body,
            organization=organization,
        )

    @mcp.tool(name="admin_upload_content")
    async def admin_upload_content(
        organization: str | None = None,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Upload content to the system
        
        Endpoint: `POST /management-rest/admin/upload-content`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            body: formdata fields as a dict.
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
            "/management-rest/admin/upload-content",
            params=None,
            json_body=body,
            organization=organization,
        )

    @mcp.tool(name="admin_upload_license")
    async def admin_upload_license(
        organization: str | None = None,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Upload license to the system
        
        Endpoint: `PUT /management-rest/admin/upload-license`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            body: Request body (JSON). Expected fields: licenseBlob.
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
            "/management-rest/admin/upload-license",
            params=None,
            json_body=body,
            organization=organization,
        )


def register_destructive(mcp: FastMCP, auth: AuthManager) -> None:
    @mcp.tool(name="admin_previous_registration_passwords")
    async def admin_previous_registration_passwords(
        passwordId: str,
        organization: str | None = None,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """This API deletes previous registration password for given id
        
        Endpoint: `DELETE /management-rest/admin/previous-registration-passwords/:passwordId`
        
        Args:
            passwordId: Path parameter (required).
            organization: Target organization in an MSSP environment (optional).
            body: Request body (JSON). Expected fields: organization.
        """
        auth.ensure(organization)
        async with FortiEDRClient(
            host=auth.config.host,
            user=auth.config.user,
            password=auth.config.password,
            default_org=auth.config.default_org,
            verify_ssl=auth.config.verify_ssl,
        ) as client:
            return await client.delete(
            f"/management-rest/admin/previous-registration-passwords/{passwordId}",
            params=None,
            json_body=body,
            organization=organization,
        )

    @mcp.tool(name="admin_set_system_mode")
    async def admin_set_system_mode(
        organization: str | None = None,
        forceAll: bool | None = None,
        mode: str | None = None,
    ) -> Any:
        """Set system modeThis API call enables you to switch the system to Simulation mode
        
        Endpoint: `PUT /management-rest/admin/set-system-mode`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            forceAll: Indicates whether to force set all the policies in 'Prevention' mode
            mode: (Required) Operation mode
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
            "/management-rest/admin/set-system-mode",
            params={
            "forceAll": forceAll,
            "mode": mode
        },
            organization=organization,
        )

