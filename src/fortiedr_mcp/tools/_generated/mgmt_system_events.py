"""Auto-generated tool stubs from FortiEDR Postman collection.

THIS FILE IS AUTO-GENERATED — DO NOT EDIT BY HAND.
To regenerate: python tools/gen_tools.py

Category: management-rest/system-events
Endpoint count: 1
"""
from __future__ import annotations

from typing import Any

from mcp.server.fastmcp import FastMCP

from ...auth import AuthManager
from ...client import FortiEDRClient



def register_read(mcp: FastMCP, auth: AuthManager) -> None:
    @mcp.tool(name="system_events_list_system_events")
    async def system_events_list_system_events(
        organization: str | None = None,
        componentNames: str | None = None,
        componentTypes: str | None = None,
        fromDate: str | None = None,
        itemsPerPage: int | None = None,
        pageNumber: int | None = None,
        sorting: str | None = None,
        strictMode: bool | None = None,
        toDate: str | None = None,
    ) -> Any:
        """Retrieve system events
        
        Endpoint: `GET /management-rest/system-events/list-system-events`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            componentNames: Specifies one or more names. The name is the customer name for license-related system events and the device name for all others events
            componentTypes: Specifies one or more component type
            fromDate: Searches for system events that occurred after this date
            itemsPerPage: An integer used for paging that indicates the number of collectors to retrieve forthe current page. The default is 100. The maximum value is 1,000
            pageNumber: An integer used for paging that indicates the required page number
            sorting: Specifies a list of strings in JSON format representing the fields by which to sort the results in the following format: %7B"column1":true, "column2":false%7D. True indicates to sort in descending order.Results are sorted by the first field, then by the second field and so on
            strictMode: A true/false parameter indicating whether to perform strict matching on the search parameters. The default is False
            toDate: Searches for system events that occurred before this date
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
            "/management-rest/system-events/list-system-events",
            params={
            "componentNames": componentNames,
            "componentTypes": componentTypes,
            "fromDate": fromDate,
            "itemsPerPage": itemsPerPage,
            "pageNumber": pageNumber,
            "sorting": sorting,
            "strictMode": strictMode,
            "toDate": toDate
        },
            organization=organization,
        )

