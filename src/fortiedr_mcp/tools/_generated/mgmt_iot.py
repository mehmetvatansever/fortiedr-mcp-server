"""Auto-generated tool stubs from FortiEDR Postman collection.

THIS FILE IS AUTO-GENERATED — DO NOT EDIT BY HAND.
To regenerate: python tools/gen_tools.py

Category: management-rest/iot
Endpoint count: 7
"""
from __future__ import annotations

from typing import Any

from mcp.server.fastmcp import FastMCP

from ...auth import AuthManager
from ...client import FortiEDRClient



def register_read(mcp: FastMCP, auth: AuthManager) -> None:
    @mcp.tool(name="iot_export_iot_json")
    async def iot_export_iot_json(
        organization: str | None = None,
        iotDeviceIds: int | None = None,
    ) -> Any:
        """This API call outputs a list of the IoT devices info
        
        Endpoint: `GET /management-rest/iot/export-iot-json`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            iotDeviceIds: (Required) Specifies the list of device ids
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
            "/management-rest/iot/export-iot-json",
            params={
            "iotDeviceIds": iotDeviceIds
        },
            organization=organization,
        )

    @mcp.tool(name="iot_list_iot_devices")
    async def iot_list_iot_devices(
        organization: str | None = None,
        categories: str | None = None,
        devices: str | None = None,
        devicesIds: int | None = None,
        firstSeenEnd: str | None = None,
        firstSeenStart: str | None = None,
        internalIps: str | None = None,
        iotGroups: str | None = None,
        iotGroupsIds: int | None = None,
        itemsPerPage: int | None = None,
        lastSeenEnd: str | None = None,
        lastSeenStart: str | None = None,
        locations: str | None = None,
        macAddresses: str | None = None,
        models: str | None = None,
        pageNumber: int | None = None,
        showExpired: bool | None = None,
        sorting: str | None = None,
        strictMode: bool | None = None,
        vendors: str | None = None,
    ) -> Any:
        """This API call outputs a list of the IoT devices in the system. Use the input parameters to filter the list
        
        Endpoint: `GET /management-rest/iot/list-iot-devices`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            categories: Specifies the list of categories values
            devices: Specifies the list of device names
            devicesIds: Specifies the list of device ids
            firstSeenEnd: Retrieves IoT devices that were first seen before the value assigned to this date. Date Format: yyyy-MM-dd HH:mm:ss
            firstSeenStart: Retrieves IoT devices that were first seen after the value assigned to this date. Date Format: yyyy-MM-dd HH:mm:ss
            internalIps: Specifies the list of IP values
            iotGroups: Specifies the list of collector group names and retrieves collectors under the given groups
            iotGroupsIds: Specifies the list of collector group ids and retrieves collectors under the given groups
            itemsPerPage: An integer used for paging that indicates the number of collectors to retrieve forthe current page. The default is 100. The maximum value is 1,000
            lastSeenEnd: Retrieves IoT devices that were last seen before the value assigned to this date. Date Format: yyyy-MM-dd HH:mm:ss
            lastSeenStart: Retrieves IoT devices that were last seen after the value assigned to this date. Date Format: yyyy-MM-dd HH:mm:ss
            locations: Specifies the list of locations values
            macAddresses: Specifies the list of mac address values
            models: Specifies the list of models values
            pageNumber: An integer used for paging that indicates the required page number
            showExpired: Specifies whether to include IoT devices which have been disconnected for more than 3 days (sequentially) and are marked as Expired
            sorting: Specifies a list of strings in JSON format representing the fields by which to sort the results in the following format: %7B"column1":true, "column2":false%7D. True indicates to sort in descending order.Results are sorted by the first field, then by the second field and so on
            strictMode: A true/false parameter indicating whether to perform strict matching on the search parameters. The default is False
            vendors: Specifies the list of vendors values
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
            "/management-rest/iot/list-iot-devices",
            params={
            "categories": categories,
            "devices": devices,
            "devicesIds": devicesIds,
            "firstSeenEnd": firstSeenEnd,
            "firstSeenStart": firstSeenStart,
            "internalIps": internalIps,
            "iotGroups": iotGroups,
            "iotGroupsIds": iotGroupsIds,
            "itemsPerPage": itemsPerPage,
            "lastSeenEnd": lastSeenEnd,
            "lastSeenStart": lastSeenStart,
            "locations": locations,
            "macAddresses": macAddresses,
            "models": models,
            "pageNumber": pageNumber,
            "showExpired": showExpired,
            "sorting": sorting,
            "strictMode": strictMode,
            "vendors": vendors
        },
            organization=organization,
        )

    @mcp.tool(name="iot_list_iot_groups")
    async def iot_list_iot_groups(
        organization: str | None = None,
    ) -> Any:
        """This API call output the IoT devices groups
        
        Endpoint: `GET /management-rest/iot/list-iot-groups`
        
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
            "/management-rest/iot/list-iot-groups",
            params=None,
            organization=organization,
        )


def register_write(mcp: FastMCP, auth: AuthManager) -> None:
    @mcp.tool(name="iot_create_iot_group")
    async def iot_create_iot_group(
        organization: str | None = None,
        name: str | None = None,
    ) -> Any:
        """This API call create IoT group
        
        Endpoint: `POST /management-rest/iot/create-iot-group`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            name: (Required) IoT group name
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
            "/management-rest/iot/create-iot-group",
            params={
            "name": name
        },
            organization=organization,
        )

    @mcp.tool(name="iot_move_iot_devices")
    async def iot_move_iot_devices(
        organization: str | None = None,
        iotDeviceIds: int | None = None,
        targetIotGroup: str | None = None,
    ) -> Any:
        """This API call move IoT devices between groups
        
        Endpoint: `PUT /management-rest/iot/move-iot-devices`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            iotDeviceIds: (Required) Array of IoT device ids
            targetIotGroup: (Required) IoT target group name
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
            "/management-rest/iot/move-iot-devices",
            params={
            "iotDeviceIds": iotDeviceIds,
            "targetIotGroup": targetIotGroup
        },
            organization=organization,
        )

    @mcp.tool(name="iot_rescan_iot_device_details")
    async def iot_rescan_iot_device_details(
        organization: str | None = None,
        categories: str | None = None,
        devices: str | None = None,
        devicesIds: int | None = None,
        firstSeenEnd: str | None = None,
        firstSeenStart: str | None = None,
        internalIps: str | None = None,
        iotGroups: str | None = None,
        iotGroupsIds: int | None = None,
        itemsPerPage: int | None = None,
        lastSeenEnd: str | None = None,
        lastSeenStart: str | None = None,
        locations: str | None = None,
        macAddresses: str | None = None,
        models: str | None = None,
        pageNumber: int | None = None,
        showExpired: bool | None = None,
        sorting: str | None = None,
        strictMode: bool | None = None,
        vendors: str | None = None,
    ) -> Any:
        """This API call device details scan on IoT device(s)
        
        Endpoint: `PUT /management-rest/iot/rescan-iot-device-details`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            categories: Specifies the list of categories values
            devices: Specifies the list of device names
            devicesIds: Specifies the list of device ids
            firstSeenEnd: Retrieves IoT devices that were first seen before the value assigned to this date. Date Format: yyyy-MM-dd HH:mm:ss
            firstSeenStart: Retrieves IoT devices that were first seen after the value assigned to this date. Date Format: yyyy-MM-dd HH:mm:ss
            internalIps: Specifies the list of IP values
            iotGroups: Specifies the list of collector group names and retrieves collectors under the given groups
            iotGroupsIds: Specifies the list of collector group ids and retrieves collectors under the given groups
            itemsPerPage: An integer used for paging that indicates the number of collectors to retrieve forthe current page. The default is 100. The maximum value is 1,000
            lastSeenEnd: Retrieves IoT devices that were last seen before the value assigned to this date. Date Format: yyyy-MM-dd HH:mm:ss
            lastSeenStart: Retrieves IoT devices that were last seen after the value assigned to this date. Date Format: yyyy-MM-dd HH:mm:ss
            locations: Specifies the list of locations values
            macAddresses: Specifies the list of mac address values
            models: Specifies the list of models values
            pageNumber: An integer used for paging that indicates the required page number
            showExpired: Specifies whether to include IoT devices which have been disconnected for more than 3 days (sequentially) and are marked as Expired
            sorting: Specifies a list of strings in JSON format representing the fields by which to sort the results in the following format: %7B"column1":true, "column2":false%7D. True indicates to sort in descending order.Results are sorted by the first field, then by the second field and so on
            strictMode: A true/false parameter indicating whether to perform strict matching on the search parameters. The default is False
            vendors: Specifies the list of vendors values
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
            "/management-rest/iot/rescan-iot-device-details",
            params={
            "categories": categories,
            "devices": devices,
            "devicesIds": devicesIds,
            "firstSeenEnd": firstSeenEnd,
            "firstSeenStart": firstSeenStart,
            "internalIps": internalIps,
            "iotGroups": iotGroups,
            "iotGroupsIds": iotGroupsIds,
            "itemsPerPage": itemsPerPage,
            "lastSeenEnd": lastSeenEnd,
            "lastSeenStart": lastSeenStart,
            "locations": locations,
            "macAddresses": macAddresses,
            "models": models,
            "pageNumber": pageNumber,
            "showExpired": showExpired,
            "sorting": sorting,
            "strictMode": strictMode,
            "vendors": vendors
        },
            organization=organization,
        )


def register_destructive(mcp: FastMCP, auth: AuthManager) -> None:
    @mcp.tool(name="iot_delete_devices")
    async def iot_delete_devices(
        organization: str | None = None,
        categories: str | None = None,
        devices: str | None = None,
        devicesIds: int | None = None,
        firstSeenEnd: str | None = None,
        firstSeenStart: str | None = None,
        internalIps: str | None = None,
        iotGroups: str | None = None,
        iotGroupsIds: int | None = None,
        itemsPerPage: int | None = None,
        lastSeenEnd: str | None = None,
        lastSeenStart: str | None = None,
        locations: str | None = None,
        macAddresses: str | None = None,
        models: str | None = None,
        pageNumber: int | None = None,
        showExpired: bool | None = None,
        sorting: str | None = None,
        strictMode: bool | None = None,
        vendors: str | None = None,
    ) -> Any:
        """This API call deletes a IoT device(s)
        
        Endpoint: `DELETE /management-rest/iot/delete-devices`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            categories: Specifies the list of categories values
            devices: Specifies the list of device names
            devicesIds: Specifies the list of device ids
            firstSeenEnd: Retrieves IoT devices that were first seen before the value assigned to this date. Date Format: yyyy-MM-dd HH:mm:ss
            firstSeenStart: Retrieves IoT devices that were first seen after the value assigned to this date. Date Format: yyyy-MM-dd HH:mm:ss
            internalIps: Specifies the list of IP values
            iotGroups: Specifies the list of collector group names and retrieves collectors under the given groups
            iotGroupsIds: Specifies the list of collector group ids and retrieves collectors under the given groups
            itemsPerPage: An integer used for paging that indicates the number of collectors to retrieve forthe current page. The default is 100. The maximum value is 1,000
            lastSeenEnd: Retrieves IoT devices that were last seen before the value assigned to this date. Date Format: yyyy-MM-dd HH:mm:ss
            lastSeenStart: Retrieves IoT devices that were last seen after the value assigned to this date. Date Format: yyyy-MM-dd HH:mm:ss
            locations: Specifies the list of locations values
            macAddresses: Specifies the list of mac address values
            models: Specifies the list of models values
            pageNumber: An integer used for paging that indicates the required page number
            showExpired: Specifies whether to include IoT devices which have been disconnected for more than 3 days (sequentially) and are marked as Expired
            sorting: Specifies a list of strings in JSON format representing the fields by which to sort the results in the following format: %7B"column1":true, "column2":false%7D. True indicates to sort in descending order.Results are sorted by the first field, then by the second field and so on
            strictMode: A true/false parameter indicating whether to perform strict matching on the search parameters. The default is False
            vendors: Specifies the list of vendors values
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
            "/management-rest/iot/delete-devices",
            params={
            "categories": categories,
            "devices": devices,
            "devicesIds": devicesIds,
            "firstSeenEnd": firstSeenEnd,
            "firstSeenStart": firstSeenStart,
            "internalIps": internalIps,
            "iotGroups": iotGroups,
            "iotGroupsIds": iotGroupsIds,
            "itemsPerPage": itemsPerPage,
            "lastSeenEnd": lastSeenEnd,
            "lastSeenStart": lastSeenStart,
            "locations": locations,
            "macAddresses": macAddresses,
            "models": models,
            "pageNumber": pageNumber,
            "showExpired": showExpired,
            "sorting": sorting,
            "strictMode": strictMode,
            "vendors": vendors
        },
            organization=organization,
        )

