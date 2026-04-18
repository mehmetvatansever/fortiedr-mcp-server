"""Auto-generated tool stubs from FortiEDR Postman collection.

THIS FILE IS AUTO-GENERATED — DO NOT EDIT BY HAND.
To regenerate: python tools/gen_tools.py

Category: management-rest/threat-hunting-exclusions
Endpoint count: 9
"""
from __future__ import annotations

from typing import Any

from mcp.server.fastmcp import FastMCP

from ...auth import AuthManager
from ...client import FortiEDRClient



def register_read(mcp: FastMCP, auth: AuthManager) -> None:
    @mcp.tool(name="threat_hunting_exclusions_exclusions_list")
    async def threat_hunting_exclusions_exclusions_list(
        organization: str | None = None,
    ) -> Any:
        """Get the list of Exclusions lists.
        
        Endpoint: `GET /management-rest/threat-hunting-exclusions/exclusions-list`
        
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
            "/management-rest/threat-hunting-exclusions/exclusions-list",
            params=None,
            organization=organization,
        )

    @mcp.tool(name="threat_hunting_exclusions_exclusions_metadata")
    async def threat_hunting_exclusions_exclusions_metadata(
        organization: str | None = None,
    ) -> Any:
        """Get the metadata and available properties for exclusions configuration. When creating/modifying an exclusion, use the response of this API as a guide for the valid attribute names and values, and thei
        
        Get the metadata and available properties for exclusions configuration. When creating/modifying an exclusion, use the response of this API as a guide for the valid attribute names and values, and their corresponding EDR event types. Every attribute corresponds to an EDR category (for example, Filename attribute corresponds with the File category), and each category is a set of EDR event types.
        
        Endpoint: `GET /management-rest/threat-hunting-exclusions/exclusions-metadata`
        
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
            "/management-rest/threat-hunting-exclusions/exclusions-metadata",
            params=None,
            organization=organization,
        )

    @mcp.tool(name="threat_hunting_exclusions_exclusions_search")
    async def threat_hunting_exclusions_exclusions_search(
        organization: str | None = None,
        os: str | None = None,
        searchText: str | None = None,
    ) -> Any:
        """Free-text search of exclusions
        
        Endpoint: `GET /management-rest/threat-hunting-exclusions/exclusions-search`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            os: OS identifiers list.
            searchText: (Required) The free text search string. The API will return every exclusion list that contains this string, or contains an exclusion with any field that contains it.
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
            "/management-rest/threat-hunting-exclusions/exclusions-search",
            params={
            "os": os,
            "searchText": searchText
        },
            organization=organization,
        )


def register_write(mcp: FastMCP, auth: AuthManager) -> None:
    @mcp.tool(name="threat_hunting_exclusions_exclusion")
    async def threat_hunting_exclusions_exclusion(
        organization: str | None = None,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Creates exclusions.
        
        Endpoint: `POST /management-rest/threat-hunting-exclusions/exclusion`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            body: Request body (JSON). Expected fields: exclusionListName, exclusions, organization.
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
            "/management-rest/threat-hunting-exclusions/exclusion",
            params=None,
            json_body=body,
            organization=organization,
        )

    @mcp.tool(name="threat_hunting_exclusions_exclusions")
    async def threat_hunting_exclusions_exclusions(
        organization: str | None = None,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Update exclusions.
        
        Endpoint: `PUT /management-rest/threat-hunting-exclusions/exclusion`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            body: Request body (JSON). Expected fields: exclusionListName, exclusions, organization.
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
            "/management-rest/threat-hunting-exclusions/exclusion",
            params=None,
            json_body=body,
            organization=organization,
        )

    @mcp.tool(name="threat_hunting_exclusions_exclusions_list")
    async def threat_hunting_exclusions_exclusions_list(
        organization: str | None = None,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Creates an exclusions list
        
        Endpoint: `POST /management-rest/threat-hunting-exclusions/exclusions-list`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            body: Request body (JSON). Expected fields: name, organization, collectorGroupIds.
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
            "/management-rest/threat-hunting-exclusions/exclusions-list",
            params=None,
            json_body=body,
            organization=organization,
        )

    @mcp.tool(name="threat_hunting_exclusions_exclusions_list")
    async def threat_hunting_exclusions_exclusions_list(
        organization: str | None = None,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Updates an exclusions list
        
        Endpoint: `PUT /management-rest/threat-hunting-exclusions/exclusions-list`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            body: Request body (JSON). Expected fields: collectorGroupIds, listName, organization, newName.
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
            "/management-rest/threat-hunting-exclusions/exclusions-list",
            params=None,
            json_body=body,
            organization=organization,
        )


def register_destructive(mcp: FastMCP, auth: AuthManager) -> None:
    @mcp.tool(name="threat_hunting_exclusions_exclusion")
    async def threat_hunting_exclusions_exclusion(
        organization: str | None = None,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Deletes one or more exclusions by Id.
        
        Endpoint: `DELETE /management-rest/threat-hunting-exclusions/exclusion`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            body: Request body (JSON). Expected fields: exclusionIds, organization.
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
            "/management-rest/threat-hunting-exclusions/exclusion",
            params=None,
            json_body=body,
            organization=organization,
        )

    @mcp.tool(name="threat_hunting_exclusions_exclusions_list")
    async def threat_hunting_exclusions_exclusions_list(
        organization: str | None = None,
        listName: str | None = None,
    ) -> Any:
        """Deletes an exclusions list.
        
        Endpoint: `DELETE /management-rest/threat-hunting-exclusions/exclusions-list`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            listName: (Required) Exclusions list name.
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
            "/management-rest/threat-hunting-exclusions/exclusions-list",
            params={
            "listName": listName
        },
            organization=organization,
        )

