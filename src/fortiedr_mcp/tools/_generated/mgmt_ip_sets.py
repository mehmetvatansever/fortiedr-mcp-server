"""Auto-generated tool stubs from FortiEDR Postman collection.

THIS FILE IS AUTO-GENERATED — DO NOT EDIT BY HAND.
To regenerate: python tools/gen_tools.py

Category: management-rest/ip-sets
Endpoint count: 4
"""
from __future__ import annotations

from typing import Any

from mcp.server.fastmcp import FastMCP

from ...auth import AuthManager
from ...client import FortiEDRClient



def register_read(mcp: FastMCP, auth: AuthManager) -> None:
    @mcp.tool(name="ip_sets_list_ip_sets")
    async def ip_sets_list_ip_sets(
        organization: str | None = None,
        ip: str | None = None,
    ) -> Any:
        """This API call outputs a list of the IP sets in the system. Use the input parameters to filter the list
        
        Endpoint: `GET /management-rest/ip-sets/list-ip-sets`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            ip: Specifies the IP of the requested sets
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
            "/management-rest/ip-sets/list-ip-sets",
            params={
            "ip": ip
        },
            organization=organization,
        )


def register_write(mcp: FastMCP, auth: AuthManager) -> None:
    @mcp.tool(name="ip_sets_create_ip_set")
    async def ip_sets_create_ip_set(
        organization: str | None = None,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """This API create IP sets in the system.
        
        This API create IP sets in the system.
Use the input parameter organization=All organizations to create for all the organization. (only for Admin role
        
        Endpoint: `POST /management-rest/ip-sets/create-ip-set`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            body: Request body (JSON). Expected fields: include, name, description, exclude, organization.
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
            "/management-rest/ip-sets/create-ip-set",
            params=None,
            json_body=body,
            organization=organization,
        )

    @mcp.tool(name="ip_sets_update_ip_set")
    async def ip_sets_update_ip_set(
        organization: str | None = None,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """This API update IP sets in the system. Use the input parameters to filter organization
        
        Endpoint: `PUT /management-rest/ip-sets/update-ip-set`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            body: Request body (JSON). Expected fields: include, name, description, exclude.
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
            "/management-rest/ip-sets/update-ip-set",
            params=None,
            json_body=body,
            organization=organization,
        )


def register_destructive(mcp: FastMCP, auth: AuthManager) -> None:
    @mcp.tool(name="ip_sets_delete_ip_set")
    async def ip_sets_delete_ip_set(
        organization: str | None = None,
        ipSets: str | None = None,
    ) -> Any:
        """This API delete IP sets from the system. Use the input parameters to filter organization
        
        Endpoint: `DELETE /management-rest/ip-sets/delete-ip-set`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            ipSets: (Required) Specifies the list of IP name to delete
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
            "/management-rest/ip-sets/delete-ip-set",
            params={
            "ipSets": ipSets
        },
            organization=organization,
        )

