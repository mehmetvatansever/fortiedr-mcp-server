"""Auto-generated tool stubs from FortiEDR Postman collection.

THIS FILE IS AUTO-GENERATED — DO NOT EDIT BY HAND.
To regenerate: python tools/gen_tools.py

Category: api/application-control
Endpoint count: 6
"""
from __future__ import annotations

from typing import Any

from mcp.server.fastmcp import FastMCP

from ...auth import AuthManager
from ...client import FortiEDRClient



def register_read(mcp: FastMCP, auth: AuthManager) -> None:
    @mcp.tool(name="application_control_applications")
    async def application_control_applications(
        organization: str | None = None,
        attributes_fileName: str | None = None,
        attributes_path: str | None = None,
        attributes_signer: str | None = None,
        currentPage: int | None = None,
        enabled: bool | None = None,
        groupIds: int | None = None,
        hash: str | None = None,
        operatingSystem: str | None = None,
        policyIds: int | None = None,
        tag: str | None = None,
    ) -> Any:
        """Get application controls
        
        Endpoint: `GET /api/application-control/applications`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            attributes_fileName: Specifies the file name, if contains special characters - encode to HTML URL Encoding
            attributes_path: Specifies the path, if contains special characters - encode to HTML URL Encoding
            attributes_signer: Specifies the value, if contains special characters - encode to HTML URL Encoding
            currentPage: (Required) Specifies the current page
            enabled: Specifies the state of the application control
            groupIds: Specifies the IDs of the relevant groups for application control
            hash: Specifies the hash of the application control
            operatingSystem: Specifies the operating system of the application control
            policyIds: Specifies the IDs of the relevant policies for application control
            tag: Specifies the tag related to application control
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
            "/api/application-control/applications",
            params={
            "attributes.fileName": attributes_fileName,
            "attributes.path": attributes_path,
            "attributes.signer": attributes_signer,
            "currentPage": currentPage,
            "enabled": enabled,
            "groupIds": groupIds,
            "hash": hash,
            "operatingSystem": operatingSystem,
            "policyIds": policyIds,
            "tag": tag
        },
            organization=organization,
        )


def register_write(mcp: FastMCP, auth: AuthManager) -> None:
    @mcp.tool(name="application_control_applications")
    async def application_control_applications(
        organization: str | None = None,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Saves new application controls and returns a list of them
        
        Endpoint: `POST /api/application-control/applications`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            body: Request body (JSON). Expected fields: applicationControls, organization.
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
            "/api/application-control/applications",
            params=None,
            json_body=body,
            organization=organization,
        )

    @mcp.tool(name="application_control_applications")
    async def application_control_applications(
        organization: str | None = None,
        appIds: int | None = None,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Edits existing application control and returns the affected ones
        
        Endpoint: `PUT /api/application-control/applications`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            appIds: (Required) The relevant application IDs to edit
            body: Request body (JSON). Expected fields: groupIds, enabled, isOverridePolicies, name, policyIds, tagId.
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
            "/api/application-control/applications",
            params={
            "appIds": appIds
        },
            json_body=body,
            organization=organization,
        )

    @mcp.tool(name="application_control_force_update_ootb_application_controls")
    async def application_control_force_update_ootb_application_controls(
        organization: str | None = None,
    ) -> Any:
        """Trigger OOTB application control update
        
        Endpoint: `POST /api/application-control/force-update-ootb-application-controls`
        
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
            return await client.post(
            "/api/application-control/force-update-ootb-application-controls",
            params=None,
            organization=organization,
        )

    @mcp.tool(name="application_control_tags")
    async def application_control_tags(
        organization: str | None = None,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Create an application control tags
        
        Endpoint: `POST /api/application-control/tags`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            body: Request body (JSON). Expected fields: name, organization.
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
            "/api/application-control/tags",
            params=None,
            json_body=body,
            organization=organization,
        )


def register_destructive(mcp: FastMCP, auth: AuthManager) -> None:
    @mcp.tool(name="application_control_applications")
    async def application_control_applications(
        organization: str | None = None,
        applicationIds: int | None = None,
    ) -> Any:
        """Deletes application controls
        
        Endpoint: `DELETE /api/application-control/applications`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            applicationIds: The IDs of the applications to be deleted
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
            "/api/application-control/applications",
            params={
            "applicationIds": applicationIds
        },
            organization=organization,
        )

