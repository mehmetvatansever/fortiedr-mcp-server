"""Auto-generated tool stubs from FortiEDR Postman collection.

THIS FILE IS AUTO-GENERATED — DO NOT EDIT BY HAND.
To regenerate: python tools/gen_tools.py

Category: management-rest/threat-hunting-settings
Endpoint count: 6
"""
from __future__ import annotations

from typing import Any

from mcp.server.fastmcp import FastMCP

from ...auth import AuthManager
from ...client import FortiEDRClient



def register_read(mcp: FastMCP, auth: AuthManager) -> None:
    @mcp.tool(name="threat_hunting_settings_threat_hunting_metadata")
    async def threat_hunting_settings_threat_hunting_metadata(
        organization: str | None = None,
    ) -> Any:
        """Get the Threat Hunting Settings metadata object, listing the available configuration options (Category and Event Types).
        
        Endpoint: `GET /management-rest/threat-hunting-settings/threat-hunting-metadata`
        
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
            "/management-rest/threat-hunting-settings/threat-hunting-metadata",
            params=None,
            organization=organization,
        )

    @mcp.tool(name="threat_hunting_settings_threat_hunting_profile")
    async def threat_hunting_settings_threat_hunting_profile(
        organization: str | None = None,
    ) -> Any:
        """Get the list of Threat Hunting Setting profiles.
        
        Endpoint: `GET /management-rest/threat-hunting-settings/threat-hunting-profile`
        
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
            "/management-rest/threat-hunting-settings/threat-hunting-profile",
            params=None,
            organization=organization,
        )


def register_write(mcp: FastMCP, auth: AuthManager) -> None:
    @mcp.tool(name="threat_hunting_settings_threat_hunting_profile_assign_collector_groups")
    async def threat_hunting_settings_threat_hunting_profile_assign_collector_groups(
        organization: str | None = None,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Update Threat Hunting profile assigned collector groups. Returns the updated list of assigned collector groups.
        
        Endpoint: `POST /management-rest/threat-hunting-settings/threat-hunting-profile/collector-groups`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            body: Request body (JSON). Expected fields: associatedCollectorGroupIds, name, organization.
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
            "/management-rest/threat-hunting-settings/threat-hunting-profile/collector-groups",
            params=None,
            json_body=body,
            organization=organization,
        )

    @mcp.tool(name="threat_hunting_settings_threat_hunting_profile")
    async def threat_hunting_settings_threat_hunting_profile(
        organization: str | None = None,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Update Threat Hunting profile
        
        Endpoint: `POST /management-rest/threat-hunting-settings/threat-hunting-profile`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            body: Request body (JSON). Expected fields: associatedCollectorGroupIds, name, organization, threatHuntingCategoryList, newName.
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
            "/management-rest/threat-hunting-settings/threat-hunting-profile",
            params=None,
            json_body=body,
            organization=organization,
        )

    @mcp.tool(name="threat_hunting_settings_threat_hunting_profile_clone")
    async def threat_hunting_settings_threat_hunting_profile_clone(
        organization: str | None = None,
        cloneProfileName: str | None = None,
        existingProfileName: str | None = None,
    ) -> Any:
        """Clone a Threat Hunting Settings profile.
        
        Endpoint: `POST /management-rest/threat-hunting-settings/threat-hunting-profile-clone`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            cloneProfileName: (Required) Cloned profile name.
            existingProfileName: (Required) Existing profile name.
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
            "/management-rest/threat-hunting-settings/threat-hunting-profile-clone",
            params={
            "cloneProfileName": cloneProfileName,
            "existingProfileName": existingProfileName
        },
            organization=organization,
        )


def register_destructive(mcp: FastMCP, auth: AuthManager) -> None:
    @mcp.tool(name="threat_hunting_settings_threat_hunting_profile")
    async def threat_hunting_settings_threat_hunting_profile(
        organization: str | None = None,
        name: str | None = None,
    ) -> Any:
        """Deletes a Threat Hunting profile.
        
        Endpoint: `DELETE /management-rest/threat-hunting-settings/threat-hunting-profile`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            name: (Required) To be deleted profile's name.
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
            "/management-rest/threat-hunting-settings/threat-hunting-profile",
            params={
            "name": name
        },
            organization=organization,
        )

