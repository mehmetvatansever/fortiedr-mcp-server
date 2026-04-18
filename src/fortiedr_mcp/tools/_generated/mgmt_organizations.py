"""Auto-generated tool stubs from FortiEDR Postman collection.

THIS FILE IS AUTO-GENERATED — DO NOT EDIT BY HAND.
To regenerate: python tools/gen_tools.py

Category: management-rest/organizations
Endpoint count: 4
"""
from __future__ import annotations

from typing import Any

from mcp.server.fastmcp import FastMCP

from ...auth import AuthManager
from ...client import FortiEDRClient



def register_read(mcp: FastMCP, auth: AuthManager) -> None:
    @mcp.tool(name="organizations_list_organizations")
    async def organizations_list_organizations(
        organization: str | None = None,
    ) -> Any:
        """This API call outputs a list of the accounts in the system.
        
        Endpoint: `GET /management-rest/organizations/list-organizations`
        
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
            "/management-rest/organizations/list-organizations",
            params=None,
            organization=organization,
        )


def register_write(mcp: FastMCP, auth: AuthManager) -> None:
    @mcp.tool(name="organizations_create_organization")
    async def organizations_create_organization(
        organization: str | None = None,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """This API creates organization in the system (only for Admin role)
        
        Endpoint: `POST /management-rest/organizations/create-organization`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            body: Request body (JSON). Expected fields: expirationDate, name, password, passwordConfirmation, eXtendedDetection, edr, edrAddOnsAllocated, edrBackupEnabled, edrEnabled, edrNumberOfShards, edrStorageAllocatedInMb, endpointsAllocated, forensics, iotAllocated, requestPolicyEngineLibUpdates, serialNumber, serversAllocated, vulnerabilityAndIoT, workstationsAllocated.
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
            "/management-rest/organizations/create-organization",
            params=None,
            json_body=body,
            organization=organization,
        )

    @mcp.tool(name="organizations_update_organization")
    async def organizations_update_organization(
        organization: str | None = None,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """This API update organization in the system (only for Admin role)
        
        Endpoint: `PUT /management-rest/organizations/update-organization`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            body: Request body (JSON). Expected fields: eXtendedDetection, edr, edrAddOnsAllocated, edrBackupEnabled, edrEnabled, edrNumberOfShards, edrStorageAllocatedInMb, endpointsAllocated, expirationDate, forensics, iotAllocated, name, requestPolicyEngineLibUpdates, serialNumber, serversAllocated, vulnerabilityAndIoT, workstationsAllocated.
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
            "/management-rest/organizations/update-organization",
            params=None,
            json_body=body,
            organization=organization,
        )


def register_destructive(mcp: FastMCP, auth: AuthManager) -> None:
    @mcp.tool(name="organizations_delete_organization")
    async def organizations_delete_organization(
        organization: str | None = None,
    ) -> Any:
        """This API delete organization in the system (only for Admin role)
        
        Endpoint: `DELETE /management-rest/organizations/delete-organization`
        
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
            return await client.delete(
            "/management-rest/organizations/delete-organization",
            params=None,
            organization=organization,
        )

