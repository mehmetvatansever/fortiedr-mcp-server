"""Auto-generated tool stubs from FortiEDR Postman collection.

THIS FILE IS AUTO-GENERATED — DO NOT EDIT BY HAND.
To regenerate: python tools/gen_tools.py

Category: management-rest/threat-hunting
Endpoint count: 15
"""
from __future__ import annotations

from typing import Any

from mcp.server.fastmcp import FastMCP

from ...auth import AuthManager
from ...client import FortiEDRClient



def register_read(mcp: FastMCP, auth: AuthManager) -> None:
    @mcp.tool(name="threat_hunting_get_syslog_servers")
    async def threat_hunting_get_syslog_servers(
        organization: str | None = None,
        accountId: int | None = None,
    ) -> Any:
        """This API get the syslog servers
        
        Endpoint: `GET /management-rest/threat-hunting/get-syslog-servers`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            accountId: (Required) accountId
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
            "/management-rest/threat-hunting/get-syslog-servers",
            params={
            "accountId": accountId
        },
            organization=organization,
        )

    @mcp.tool(name="threat_hunting_list_saved_queries")
    async def threat_hunting_list_saved_queries(
        organization: str | None = None,
        scheduled: bool | None = None,
        source: str | None = None,
    ) -> Any:
        """This API retrieves the existing saved queries list
        
        Endpoint: `GET /management-rest/threat-hunting/list-saved-queries`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            scheduled: A true/false parameter indicating whether the query is scheduled
            source: Specifies the query source list
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
            "/management-rest/threat-hunting/list-saved-queries",
            params={
            "scheduled": scheduled,
            "source": source
        },
            organization=organization,
        )

    @mcp.tool(name="threat_hunting_list_tags")
    async def threat_hunting_list_tags(
        organization: str | None = None,
    ) -> Any:
        """This API retrieves the existing saved queries tag list
        
        Endpoint: `GET /management-rest/threat-hunting/list-tags`
        
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
            "/management-rest/threat-hunting/list-tags",
            params=None,
            organization=organization,
        )


def register_write(mcp: FastMCP, auth: AuthManager) -> None:
    @mcp.tool(name="threat_hunting_counts")
    async def threat_hunting_counts(
        organization: str | None = None,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """This API call outputs EDR total events for every EDR category
        
        Endpoint: `POST /management-rest/threat-hunting/counts`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            body: Request body (JSON). Expected fields: accountId, category, devices, filters, fromTime, itemsPerPage, organization, pageNumber, query, sorting, time, toTime.
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
            "/management-rest/threat-hunting/counts",
            params=None,
            json_body=body,
            organization=organization,
        )

    @mcp.tool(name="threat_hunting_create_or_edit_tag")
    async def threat_hunting_create_or_edit_tag(
        organization: str | None = None,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """This API creates or edits the saved queries tag
        
        Endpoint: `POST /management-rest/threat-hunting/create-or-edit-tag`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            body: Request body (JSON). Expected fields: newTagName, organization, tagId, tagName.
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
            "/management-rest/threat-hunting/create-or-edit-tag",
            params=None,
            json_body=body,
            organization=organization,
        )

    @mcp.tool(name="threat_hunting_customize_fortinet_query")
    async def threat_hunting_customize_fortinet_query(
        organization: str | None = None,
        id: int | None = None,
        queryToEdit: str | None = None,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """This API customizes the scheduling properties of a Fortinet query
        
        Endpoint: `POST /management-rest/threat-hunting/customize-fortinet-query`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            id: Specifies the query ID to edit
            queryToEdit: Specifies the query name to edit
            body: Request body (JSON). Expected fields: organization, dayOfMonth, dayOfWeek, forceSaving, frequency, frequencyUnit, fromTime, hour, scheduled, state, time, toTime.
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
            "/management-rest/threat-hunting/customize-fortinet-query",
            params={
            "id": id,
            "queryToEdit": queryToEdit
        },
            json_body=body,
            organization=organization,
        )

    @mcp.tool(name="threat_hunting_facets")
    async def threat_hunting_facets(
        organization: str | None = None,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """This API retrieves EDR total events for every EDR facet item
        
        Endpoint: `POST /management-rest/threat-hunting/facets`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            body: Request body (JSON). Expected fields: facets, accountId, category, devices, filters, fromTime, itemsPerPage, organization, pageNumber, query, sorting, time, toTime.
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
            "/management-rest/threat-hunting/facets",
            params=None,
            json_body=body,
            organization=organization,
        )

    @mcp.tool(name="threat_hunting_save_query")
    async def threat_hunting_save_query(
        organization: str | None = None,
        id: int | None = None,
        queryToEdit: str | None = None,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """This API saves the query
        
        Endpoint: `POST /management-rest/threat-hunting/save-query`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            id: Specifies the query ID to edit
            queryToEdit: Specifies the query name to edit
            body: Request body (JSON). Expected fields: organization, category, classification, collectorNames, community, dayOfMonth, dayOfWeek, description, forceSaving, frequency, frequencyUnit, fromTime, hour, name, query, scheduled, state, tagIds, tagNames, time, toTime.
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
            "/management-rest/threat-hunting/save-query",
            params={
            "id": id,
            "queryToEdit": queryToEdit
        },
            json_body=body,
            organization=organization,
        )

    @mcp.tool(name="threat_hunting_search")
    async def threat_hunting_search(
        organization: str | None = None,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """This API call outputs a list of Activity events from middleware.
        
        Endpoint: `POST /management-rest/threat-hunting/search`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            body: Request body (JSON). Expected fields: accountId, category, devices, filters, fromTime, itemsPerPage, organization, pageNumber, query, sorting, time, toTime.
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
            "/management-rest/threat-hunting/search",
            params=None,
            json_body=body,
            organization=organization,
        )

    @mcp.tool(name="threat_hunting_set_query_state")
    async def threat_hunting_set_query_state(
        organization: str | None = None,
        markAll: bool | None = None,
        queryIds: int | None = None,
        queryNames: str | None = None,
        source: str | None = None,
        state: bool | None = None,
    ) -> Any:
        """This API updates the scheduled saved query state
        
        Endpoint: `PUT /management-rest/threat-hunting/set-query-state`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            markAll: A true/false parameter indicating whether all queries should be marked with the same value as 'state' property. False by default
            queryIds: Specifies the query ID list
            queryNames: Specifies the query name list
            source: Specifies the query source list
            state: (Required) A true/false parameter indicating whether to save the query as enabled
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
            "/management-rest/threat-hunting/set-query-state",
            params={
            "markAll": markAll,
            "queryIds": queryIds,
            "queryNames": queryNames,
            "source": source,
            "state": state
        },
            organization=organization,
        )

    @mcp.tool(name="threat_hunting_test_syslog_server")
    async def threat_hunting_test_syslog_server(
        organization: str | None = None,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """This API test a syslog server connection
        
        Endpoint: `POST /management-rest/threat-hunting/test-syslog-server`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            body: Request body (JSON). Expected fields: accountId, host, id, name, port, protocol, syslogRFCFormat, useSSL.
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
            "/management-rest/threat-hunting/test-syslog-server",
            params=None,
            json_body=body,
            organization=organization,
        )

    @mcp.tool(name="threat_hunting_update_syslog_server")
    async def threat_hunting_update_syslog_server(
        organization: str | None = None,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """This API update a syslog server
        
        Endpoint: `POST /management-rest/threat-hunting/update-syslog-server`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            body: Request body (JSON). Expected fields: accountId, agentGroupIds, host, id, name, port, protocol, syslogRFCFormat, useSSL.
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
            "/management-rest/threat-hunting/update-syslog-server",
            params=None,
            json_body=body,
            organization=organization,
        )


def register_destructive(mcp: FastMCP, auth: AuthManager) -> None:
    @mcp.tool(name="threat_hunting_delete_saved_queries")
    async def threat_hunting_delete_saved_queries(
        organization: str | None = None,
        deleteAll: bool | None = None,
        deleteFromCommunity: bool | None = None,
        queryIds: int | None = None,
        queryNames: str | None = None,
        scheduled: bool | None = None,
        source: str | None = None,
    ) -> Any:
        """This API deletes the saved queries
        
        Endpoint: `DELETE /management-rest/threat-hunting/delete-saved-queries`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            deleteAll: A true/false parameter indicating whether all queries should be deleted. False by default
            deleteFromCommunity: A true/false parameter indicating if whether to delete a query from the FortiEDR Community also
            queryIds: Specifies the query IDs list
            queryNames: Specifies the query names list
            scheduled: A true/false parameter indicating whether the query is scheduled
            source: Specifies the query source list
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
            "/management-rest/threat-hunting/delete-saved-queries",
            params={
            "deleteAll": deleteAll,
            "deleteFromCommunity": deleteFromCommunity,
            "queryIds": queryIds,
            "queryNames": queryNames,
            "scheduled": scheduled,
            "source": source
        },
            organization=organization,
        )

    @mcp.tool(name="threat_hunting_delete_syslog_server")
    async def threat_hunting_delete_syslog_server(
        organization: str | None = None,
        id: int | None = None,
    ) -> Any:
        """This API delete a syslog server
        
        Endpoint: `DELETE /management-rest/threat-hunting/delete-syslog-server`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            id: (Required) id
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
            "/management-rest/threat-hunting/delete-syslog-server",
            params={
            "id": id
        },
            organization=organization,
        )

    @mcp.tool(name="threat_hunting_delete_tags")
    async def threat_hunting_delete_tags(
        organization: str | None = None,
        tagIds: int | None = None,
        tagNames: str | None = None,
    ) -> Any:
        """This API deletes the saved queries tags
        
        Endpoint: `DELETE /management-rest/threat-hunting/delete-tags`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            tagIds: Specifies the tag ID list
            tagNames: Specifies the tag name list
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
            "/management-rest/threat-hunting/delete-tags",
            params={
            "tagIds": tagIds,
            "tagNames": tagNames
        },
            organization=organization,
        )

