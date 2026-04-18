"""Auto-generated tool stubs from FortiEDR Postman collection.

THIS FILE IS AUTO-GENERATED — DO NOT EDIT BY HAND.
To regenerate: python tools/gen_tools.py

Category: management-rest/inventory
Endpoint count: 23
"""
from __future__ import annotations

from typing import Any

from mcp.server.fastmcp import FastMCP

from ...auth import AuthManager
from ...client import FortiEDRClient



def register_read(mcp: FastMCP, auth: AuthManager) -> None:
    @mcp.tool(name="inventory_aggregator_logs")
    async def inventory_aggregator_logs(
        organization: str | None = None,
        device: str | None = None,
        deviceId: int | None = None,
    ) -> Any:
        """This API call retrieves a aggregator logs
        
        Endpoint: `GET /management-rest/inventory/aggregator-logs`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            device: Specifies the name of the device
            deviceId: Specifies the ID of the device
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
            "/management-rest/inventory/aggregator-logs",
            params={
            "device": device,
            "deviceId": deviceId
        },
            organization=organization,
        )

    @mcp.tool(name="inventory_check_custom_installer")
    async def inventory_check_custom_installer(
        organization: str | None = None,
        customInstallerID: str | None = None,
    ) -> Any:
        """This API call for checking the results for an custom installer request and getting the installer url
        
        Endpoint: `GET /management-rest/inventory/check-custom-installer`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            customInstallerID: (Required) customInstallerID
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
            "/management-rest/inventory/check-custom-installer",
            params={
            "customInstallerID": customInstallerID
        },
            organization=organization,
        )

    @mcp.tool(name="inventory_collector_logs")
    async def inventory_collector_logs(
        organization: str | None = None,
        device: str | None = None,
        deviceId: int | None = None,
    ) -> Any:
        """This API call retrieves a collector logs
        
        Endpoint: `GET /management-rest/inventory/collector-logs`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            device: Specifies the name of the device
            deviceId: Specifies the ID of the device
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
            "/management-rest/inventory/collector-logs",
            params={
            "device": device,
            "deviceId": deviceId
        },
            organization=organization,
        )

    @mcp.tool(name="inventory_core_logs")
    async def inventory_core_logs(
        organization: str | None = None,
        device: str | None = None,
        deviceId: int | None = None,
    ) -> Any:
        """This API call retrieves a core logs
        
        Endpoint: `GET /management-rest/inventory/core-logs`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            device: Specifies the name of the device
            deviceId: Specifies the ID of the device
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
            "/management-rest/inventory/core-logs",
            params={
            "device": device,
            "deviceId": deviceId
        },
            organization=organization,
        )

    @mcp.tool(name="inventory_list_aggregators")
    async def inventory_list_aggregators(
        organization: str | None = None,
        ip: str | None = None,
        names: str | None = None,
        versions: str | None = None,
    ) -> Any:
        """This API call output the list of aggregators
        
        Endpoint: `GET /management-rest/inventory/list-aggregators`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            ip: IP
            names: List of aggregators names
            versions: List of aggregators versions
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
            "/management-rest/inventory/list-aggregators",
            params={
            "ip": ip,
            "names": names,
            "versions": versions
        },
            organization=organization,
        )

    @mcp.tool(name="inventory_list_collector_groups")
    async def inventory_list_collector_groups(
        organization: str | None = None,
    ) -> Any:
        """This API call output the collectors groups
        
        Endpoint: `GET /management-rest/inventory/list-collector-groups`
        
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
            "/management-rest/inventory/list-collector-groups",
            params=None,
            organization=organization,
        )

    @mcp.tool(name="inventory_list_collectors")
    async def inventory_list_collectors(
        organization: str | None = None,
        cloudAccounts: str | None = None,
        cloudProviders: str | None = None,
        clusters: str | None = None,
        collectorGroups: str | None = None,
        collectorGroupsIds: int | None = None,
        collectorType: str | None = None,
        devices: str | None = None,
        devicesIds: int | None = None,
        firstSeen: str | None = None,
        hasCrashDumps: bool | None = None,
        ips: str | None = None,
        itemsPerPage: int | None = None,
        lastSeenEnd: str | None = None,
        lastSeenStart: str | None = None,
        loggedUser: str | None = None,
        operatingSystems: str | None = None,
        osFamilies: str | None = None,
        pageNumber: int | None = None,
        showExpired: bool | None = None,
        sorting: str | None = None,
        states: str | None = None,
        strictMode: bool | None = None,
        versions: str | None = None,
    ) -> Any:
        """This API call outputs a list of the Collectors in the system. Use the input parameters to filter the list
        
        Endpoint: `GET /management-rest/inventory/list-collectors`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            cloudAccounts: Specifies the list cloud account names
            cloudProviders: Specifies the list of cloud providers: AWS, Azure, GCP
            clusters: Specifies the list of cluster
            collectorGroups: Specifies the list of collector group names and retrieves collectors under the
given groups
            collectorGroupsIds: Specifies the list of collector group Ids and retrieves collectors under the
given groups
            collectorType: Specifies the group types of the collectors. Types: All, Collector, Workloads. All by default
            devices: Specifies the list of device names
            devicesIds: Specifies the list of device ids
            firstSeen: Retrieves collectors that were first seen after the value assigned to this date. Date Format: yyyy-MM-dd HH:mm:ss
            hasCrashDumps: Retrieves collectors that have crash dumps
            ips: Specifies the list of IP values
            itemsPerPage: An integer used for paging that indicates the number of collectors to retrieve forthe current page. The default is 100. The maximum value is 1,000
            lastSeenEnd: Retrieves collectors that were last seen before the value assigned to this date. Date Format: yyyy-MM-dd HH:mm:ss
            lastSeenStart: Retrieves collectors that were last seen after the value assigned to this date. Date Format: yyyy-MM-dd HH:mm:ss
            loggedUser: Specifies the user that was logged when the event occurred
            operatingSystems: Specifies the list of specific operating systems. For example, Windows 7 Pro
            osFamilies: Specifies the list of operating system families: Windows, Windows Server or OS X
            pageNumber: An integer used for paging that indicates the required page number
            showExpired: Specifies whether to include collectors which have been disconnected for more than 30 days (sequentially) and are marked as Expired
            sorting: Specifies a list of strings in JSON format representing the fields by which to sort the results in the following format: %7B"column1":true, "column2":false%7D. True indicates to sort in descending order.Results are sorted by the first field, then by the second field and so on
            states: Specifies the list of collector states: Running, Disconnected, Disabled, Degraded, 
Pending Reboot, Isolated, Expired, Migrated or Pending Migration
            strictMode: A true/false parameter indicating whether to perform strict matching on the search parameters. The default is False
            versions: Specifies the list of collector versions
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
            "/management-rest/inventory/list-collectors",
            params={
            "cloudAccounts": cloudAccounts,
            "cloudProviders": cloudProviders,
            "clusters": clusters,
            "collectorGroups": collectorGroups,
            "collectorGroupsIds": collectorGroupsIds,
            "collectorType": collectorType,
            "devices": devices,
            "devicesIds": devicesIds,
            "firstSeen": firstSeen,
            "hasCrashDumps": hasCrashDumps,
            "ips": ips,
            "itemsPerPage": itemsPerPage,
            "lastSeenEnd": lastSeenEnd,
            "lastSeenStart": lastSeenStart,
            "loggedUser": loggedUser,
            "operatingSystems": operatingSystems,
            "osFamilies": osFamilies,
            "pageNumber": pageNumber,
            "showExpired": showExpired,
            "sorting": sorting,
            "states": states,
            "strictMode": strictMode,
            "versions": versions
        },
            organization=organization,
        )

    @mcp.tool(name="inventory_list_cores")
    async def inventory_list_cores(
        organization: str | None = None,
        deploymentModes: str | None = None,
        hasCrashDumps: bool | None = None,
        ip: str | None = None,
        names: str | None = None,
        versions: str | None = None,
    ) -> Any:
        """This API call output the list of cores
        
        Endpoint: `GET /management-rest/inventory/list-cores`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            deploymentModes: List of cores deployments modes
            hasCrashDumps: Has crash dumps
            ip: IP
            names: List of cores names
            versions: List of cores versions
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
            "/management-rest/inventory/list-cores",
            params={
            "deploymentModes": deploymentModes,
            "hasCrashDumps": hasCrashDumps,
            "ip": ip,
            "names": names,
            "versions": versions
        },
            organization=organization,
        )

    @mcp.tool(name="inventory_list_repositories")
    async def inventory_list_repositories(
        organization: str | None = None,
    ) -> Any:
        """This API call output the list of repositories (edrs)
        
        Endpoint: `GET /management-rest/inventory/list-repositories`
        
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
            "/management-rest/inventory/list-repositories",
            params=None,
            organization=organization,
        )

    @mcp.tool(name="inventory_list_unmanaged_devices")
    async def inventory_list_unmanaged_devices(
        organization: str | None = None,
        itemsPerPage: int | None = None,
        pageNumber: int | None = None,
        sorting: str | None = None,
        strictMode: bool | None = None,
    ) -> Any:
        """This API call outputs a list of the unmanaged devices in the system
        
        Endpoint: `GET /management-rest/inventory/list-unmanaged-devices`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            itemsPerPage: An integer used for paging that indicates the number of collectors to retrieve forthe current page. The default is 100. The maximum value is 1,000
            pageNumber: An integer used for paging that indicates the required page number
            sorting: Specifies a list of strings in JSON format representing the fields by which to sort the results in the following format: %7B"column1":true, "column2":false%7D. True indicates to sort in descending order.Results are sorted by the first field, then by the second field and so on
            strictMode: A true/false parameter indicating whether to perform strict matching on the search parameters. The default is False
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
            "/management-rest/inventory/list-unmanaged-devices",
            params={
            "itemsPerPage": itemsPerPage,
            "pageNumber": pageNumber,
            "sorting": sorting,
            "strictMode": strictMode
        },
            organization=organization,
        )

    @mcp.tool(name="inventory_system_logs")
    async def inventory_system_logs(
        organization: str | None = None,
    ) -> Any:
        """This API call retrieves a system logs
        
        Endpoint: `GET /management-rest/inventory/system-logs`
        
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
            "/management-rest/inventory/system-logs",
            params=None,
            organization=organization,
        )


def register_write(mcp: FastMCP, auth: AuthManager) -> None:
    @mcp.tool(name="inventory_create_collector_group")
    async def inventory_create_collector_group(
        organization: str | None = None,
        name: str | None = None,
    ) -> Any:
        """This API call create collector group
        
        Endpoint: `POST /management-rest/inventory/create-collector-group`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            name: (Required) Collector group name
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
            "/management-rest/inventory/create-collector-group",
            params={
            "name": name
        },
            organization=organization,
        )

    @mcp.tool(name="inventory_create_ems_custom_installer")
    async def inventory_create_ems_custom_installer(
        organization: str | None = None,
        aggregatorAddress: str | None = None,
        aggregatorPort: int | None = None,
        citrixPVS: bool | None = None,
        collectorGroup: str | None = None,
        collectorVersion: str | None = None,
        distro: str | None = None,
        is64bit: bool | None = None,
        osType: str | None = None,
        proxy: bool | None = None,
        vdi: bool | None = None,
    ) -> Any:
        """This API call sends request for creating custom-installer for EMS integration
        
        Endpoint: `POST /management-rest/inventory/create-ems-custom-installer`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            aggregatorAddress: Specifies the aggregator ip or dns address
            aggregatorPort: Specifies the aggregator port
            citrixPVS: Specifies whether the collector installed with citrix in pvs mode
            collectorGroup: Specifies the requested collector group
            collectorVersion: Specifies the requested collector version
            distro: Specifies the Linux distribution. For example: CentOS_6, CentOS_7, CentOS_8, CentOS_9, Amazon, Oracle_6, Oracle_7, Oracle_8, SLES_12, SLES_15, Ubuntu_16.04, Ubuntu_18.04, Ubuntu_20.04, Ubuntu_22.04
            is64bit: Specifies the Windows os bit version
            osType: (Required) Specifies the operating system type
            proxy: Specifies the system proxy settings (Only applies to Collector versions 3.1 and above)
            vdi: Specifies the VDI (Virtual Desktop Infrastructure) installation
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
            "/management-rest/inventory/create-ems-custom-installer",
            params={
            "aggregatorAddress": aggregatorAddress,
            "aggregatorPort": aggregatorPort,
            "citrixPVS": citrixPVS,
            "collectorGroup": collectorGroup,
            "collectorVersion": collectorVersion,
            "distro": distro,
            "is64bit": is64bit,
            "osType": osType,
            "proxy": proxy,
            "vdi": vdi
        },
            organization=organization,
        )

    @mcp.tool(name="inventory_move_collectors")
    async def inventory_move_collectors(
        organization: str | None = None,
        collectorIds: int | None = None,
        collectorSIDs: str | None = None,
        collectors: str | None = None,
        forceAssign: bool | None = None,
        targetCollectorGroup: str | None = None,
    ) -> Any:
        """This API call move collector between groups
        
        Endpoint: `PUT /management-rest/inventory/move-collectors`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            collectorIds: value = Array of collectors Ids. To move collectors from one organization to another
            collectorSIDs: value = Array of collectors SIDS. To move collectors from one organization to another
            collectors: Array of collectors names. To move collectors from one organization to another, for each collector please add the organization name before the collector name (<organization-name>//<collector-name>)
            forceAssign: Indicates whether to force the assignment even if the organization of the target Collector group is under migration
            targetCollectorGroup: (Required) Collector group. To move collectors from one organization to another, please add the organization name before the target collector group (<organization-name>//<collector-group-name>)
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
            "/management-rest/inventory/move-collectors",
            params={
            "collectorIds": collectorIds,
            "collectorSIDs": collectorSIDs,
            "collectors": collectors,
            "forceAssign": forceAssign,
            "targetCollectorGroup": targetCollectorGroup
        },
            organization=organization,
        )

    @mcp.tool(name="inventory_movecollectorstoanotheraggregator")
    async def inventory_movecollectorstoanotheraggregator(
        organization: str | None = None,
        address: str | None = None,
        cloudAccounts: str | None = None,
        cloudProviders: str | None = None,
        clusters: str | None = None,
        collectorGroups: str | None = None,
        collectorGroupsIds: int | None = None,
        collectorType: str | None = None,
        destinationAccountName: str | None = None,
        devices: str | None = None,
        devicesIds: int | None = None,
        firstSeen: str | None = None,
        hasCrashDumps: bool | None = None,
        ips: str | None = None,
        itemsPerPage: int | None = None,
        lastSeenEnd: str | None = None,
        lastSeenStart: str | None = None,
        loggedUser: str | None = None,
        operatingSystems: str | None = None,
        osFamilies: str | None = None,
        pageNumber: int | None = None,
        showExpired: bool | None = None,
        sorting: str | None = None,
        states: str | None = None,
        strictMode: bool | None = None,
        versions: str | None = None,
    ) -> Any:
        """This API call starts collectors transfer to another aggregator. Use the input parameters to filter the list
        
        Endpoint: `POST /management-rest/inventory/moveCollectorsToAnotherAggregator`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            address: Specifies the address of the destination aggregator
            cloudAccounts: Specifies the list cloud account names
            cloudProviders: Specifies the list of cloud providers: AWS, Azure, GCP
            clusters: Specifies the list of cluster
            collectorGroups: Specifies the list of collector group names and retrieves collectors under the
given groups
            collectorGroupsIds: Specifies the list of collector group Ids and retrieves collectors under the
given groups
            collectorType: Specifies the group types of the collectors. Types: All, Collector, Workloads. All by default
            destinationAccountName: Specifies the name of the destination account
            devices: Specifies the list of device names
            devicesIds: Specifies the list of device ids
            firstSeen: Retrieves collectors that were first seen after the value assigned to this date. Date Format: yyyy-MM-dd HH:mm:ss
            hasCrashDumps: Retrieves collectors that have crash dumps
            ips: Specifies the list of IP values
            itemsPerPage: An integer used for paging that indicates the number of collectors to retrieve forthe current page. The default is 100. The maximum value is 1,000
            lastSeenEnd: Retrieves collectors that were last seen before the value assigned to this date. Date Format: yyyy-MM-dd HH:mm:ss
            lastSeenStart: Retrieves collectors that were last seen after the value assigned to this date. Date Format: yyyy-MM-dd HH:mm:ss
            loggedUser: Specifies the user that was logged when the event occurred
            operatingSystems: Specifies the list of specific operating systems. For example, Windows 7 Pro
            osFamilies: Specifies the list of operating system families: Windows, Windows Server or OS X
            pageNumber: An integer used for paging that indicates the required page number
            showExpired: Specifies whether to include collectors which have been disconnected for more than 30 days (sequentially) and are marked as Expired
            sorting: Specifies a list of strings in JSON format representing the fields by which to sort the results in the following format: %7B"column1":true, "column2":false%7D. True indicates to sort in descending order.Results are sorted by the first field, then by the second field and so on
            states: Specifies the list of collector states: Running, Disconnected, Disabled, Degraded, 
Pending Reboot, Isolated, Expired, Migrated or Pending Migration
            strictMode: A true/false parameter indicating whether to perform strict matching on the search parameters. The default is False
            versions: Specifies the list of collector versions
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
            "/management-rest/inventory/moveCollectorsToAnotherAggregator",
            params={
            "address": address,
            "cloudAccounts": cloudAccounts,
            "cloudProviders": cloudProviders,
            "clusters": clusters,
            "collectorGroups": collectorGroups,
            "collectorGroupsIds": collectorGroupsIds,
            "collectorType": collectorType,
            "destinationAccountName": destinationAccountName,
            "devices": devices,
            "devicesIds": devicesIds,
            "firstSeen": firstSeen,
            "hasCrashDumps": hasCrashDumps,
            "ips": ips,
            "itemsPerPage": itemsPerPage,
            "lastSeenEnd": lastSeenEnd,
            "lastSeenStart": lastSeenStart,
            "loggedUser": loggedUser,
            "operatingSystems": operatingSystems,
            "osFamilies": osFamilies,
            "pageNumber": pageNumber,
            "showExpired": showExpired,
            "sorting": sorting,
            "states": states,
            "strictMode": strictMode,
            "versions": versions
        },
            organization=organization,
        )

    @mcp.tool(name="inventory_update_collector_group_name")
    async def inventory_update_collector_group_name(
        organization: str | None = None,
        collectorGroupId: int | None = None,
        groupName: str | None = None,
    ) -> Any:
        """This API updates collector group name!
        
        Endpoint: `PUT /management-rest/inventory/update-collector-group-name`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            collectorGroupId: (Required) Collector Group id
            groupName: (Required) New group name
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
            "/management-rest/inventory/update-collector-group-name",
            params={
            "collectorGroupId": collectorGroupId,
            "groupName": groupName
        },
            organization=organization,
        )


def register_destructive(mcp: FastMCP, auth: AuthManager) -> None:
    @mcp.tool(name="inventory_delete_collectors")
    async def inventory_delete_collectors(
        organization: str | None = None,
        cloudAccounts: str | None = None,
        cloudProviders: str | None = None,
        clusters: str | None = None,
        collectorGroups: str | None = None,
        collectorGroupsIds: int | None = None,
        collectorType: str | None = None,
        confirmDeletion: bool | None = None,
        deleteAll: bool | None = None,
        devices: str | None = None,
        devicesIds: int | None = None,
        firstSeen: str | None = None,
        hasCrashDumps: bool | None = None,
        ips: str | None = None,
        itemsPerPage: int | None = None,
        lastSeenEnd: str | None = None,
        lastSeenStart: str | None = None,
        loggedUser: str | None = None,
        operatingSystems: str | None = None,
        osFamilies: str | None = None,
        pageNumber: int | None = None,
        showExpired: bool | None = None,
        sorting: str | None = None,
        states: str | None = None,
        strictMode: bool | None = None,
        versions: str | None = None,
    ) -> Any:
        """This API call deletes a Collector(s)
        
        Endpoint: `DELETE /management-rest/inventory/delete-collectors`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            cloudAccounts: Specifies the list cloud account names
            cloudProviders: Specifies the list of cloud providers: AWS, Azure, GCP
            clusters: Specifies the list of cluster
            collectorGroups: Specifies the list of collector group names and retrieves collectors under the
given groups
            collectorGroupsIds: Specifies the list of collector group Ids and retrieves collectors under the
given groups
            collectorType: Specifies the group types of the collectors. Types: All, Collector, Workloads. All by default
            confirmDeletion: A true/false parameter indicating if to detach/delete relevant exceptions from Collector groups about to be deleted
            deleteAll: A true/false parameter indicating if all collectors should be deleted
            devices: Specifies the list of device names
            devicesIds: Specifies the list of device ids
            firstSeen: Retrieves collectors that were first seen after the value assigned to this date. Date Format: yyyy-MM-dd HH:mm:ss
            hasCrashDumps: Retrieves collectors that have crash dumps
            ips: Specifies the list of IP values
            itemsPerPage: An integer used for paging that indicates the number of collectors to retrieve forthe current page. The default is 100. The maximum value is 1,000
            lastSeenEnd: Retrieves collectors that were last seen before the value assigned to this date. Date Format: yyyy-MM-dd HH:mm:ss
            lastSeenStart: Retrieves collectors that were last seen after the value assigned to this date. Date Format: yyyy-MM-dd HH:mm:ss
            loggedUser: Specifies the user that was logged when the event occurred
            operatingSystems: Specifies the list of specific operating systems. For example, Windows 7 Pro
            osFamilies: Specifies the list of operating system families: Windows, Windows Server or OS X
            pageNumber: An integer used for paging that indicates the required page number
            showExpired: Specifies whether to include collectors which have been disconnected for more than 30 days (sequentially) and are marked as Expired
            sorting: Specifies a list of strings in JSON format representing the fields by which to sort the results in the following format: %7B"column1":true, "column2":false%7D. True indicates to sort in descending order.Results are sorted by the first field, then by the second field and so on
            states: Specifies the list of collector states: Running, Disconnected, Disabled, Degraded, 
Pending Reboot, Isolated, Expired, Migrated or Pending Migration
            strictMode: A true/false parameter indicating whether to perform strict matching on the search parameters. The default is False
            versions: Specifies the list of collector versions
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
            "/management-rest/inventory/delete-collectors",
            params={
            "cloudAccounts": cloudAccounts,
            "cloudProviders": cloudProviders,
            "clusters": clusters,
            "collectorGroups": collectorGroups,
            "collectorGroupsIds": collectorGroupsIds,
            "collectorType": collectorType,
            "confirmDeletion": confirmDeletion,
            "deleteAll": deleteAll,
            "devices": devices,
            "devicesIds": devicesIds,
            "firstSeen": firstSeen,
            "hasCrashDumps": hasCrashDumps,
            "ips": ips,
            "itemsPerPage": itemsPerPage,
            "lastSeenEnd": lastSeenEnd,
            "lastSeenStart": lastSeenStart,
            "loggedUser": loggedUser,
            "operatingSystems": operatingSystems,
            "osFamilies": osFamilies,
            "pageNumber": pageNumber,
            "showExpired": showExpired,
            "sorting": sorting,
            "states": states,
            "strictMode": strictMode,
            "versions": versions
        },
            organization=organization,
        )

    @mcp.tool(name="inventory_ems_move_collectors")
    async def inventory_ems_move_collectors(
        organization: str | None = None,
        collectorIds: int | None = None,
        collectorSIDs: str | None = None,
        collectors: str | None = None,
        forceAssign: bool | None = None,
        targetCollectorGroup: str | None = None,
    ) -> Any:
        """This API call move collector between groups for EMS integration
        
        Endpoint: `PUT /management-rest/inventory/ems-move-collectors`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            collectorIds: value = Array of collectors Ids. To move collectors from one organization to another
            collectorSIDs: value = Array of collectors SIDS. To move collectors from one organization to another
            collectors: Array of collectors names. To move collectors from one organization to another, for each collector please add the organization name before the collector name (<organization-name>//<collector-name>)
            forceAssign: Indicates whether to force the assignment even if the organization of the target Collector group is under migration
            targetCollectorGroup: (Required) Collector group. To move collectors from one organization to another, please add the organization name before the target collector group (<organization-name>//<collector-group-name>)
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
            "/management-rest/inventory/ems-move-collectors",
            params={
            "collectorIds": collectorIds,
            "collectorSIDs": collectorSIDs,
            "collectors": collectors,
            "forceAssign": forceAssign,
            "targetCollectorGroup": targetCollectorGroup
        },
            organization=organization,
        )

    @mcp.tool(name="inventory_isolate_collectors")
    async def inventory_isolate_collectors(
        organization: str | None = None,
        devices: str | None = None,
        devicesIds: int | None = None,
    ) -> Any:
        """This API call isolate collector functionality
        
        Endpoint: `PUT /management-rest/inventory/isolate-collectors`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            devices: Specifies the list of device names
            devicesIds: Specifies the list of device ids
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
            "/management-rest/inventory/isolate-collectors",
            params={
            "devices": devices,
            "devicesIds": devicesIds
        },
            organization=organization,
        )

    @mcp.tool(name="inventory_release_license")
    async def inventory_release_license(
        organization: str | None = None,
        cloudAccounts: str | None = None,
        cloudProviders: str | None = None,
        clusters: str | None = None,
        collectorGroups: str | None = None,
        collectorGroupsIds: int | None = None,
        collectorType: str | None = None,
        devices: str | None = None,
        devicesIds: int | None = None,
        firstSeen: str | None = None,
        hasCrashDumps: bool | None = None,
        ips: str | None = None,
        itemsPerPage: int | None = None,
        lastSeenEnd: str | None = None,
        lastSeenStart: str | None = None,
        loggedUser: str | None = None,
        operatingSystems: str | None = None,
        osFamilies: str | None = None,
        pageNumber: int | None = None,
        releaseLicense: bool | None = None,
        showExpired: bool | None = None,
        sorting: str | None = None,
        states: str | None = None,
        strictMode: bool | None = None,
        versions: str | None = None,
    ) -> Any:
        """This API call enables/disables a Collector(s) and release it license. You must specify whether the License must be released or acquired! Cooldown between the requests should be 2-3 minutes!
        
        Endpoint: `PUT /management-rest/inventory/release-license`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            cloudAccounts: Specifies the list cloud account names
            cloudProviders: Specifies the list of cloud providers: AWS, Azure, GCP
            clusters: Specifies the list of cluster
            collectorGroups: Specifies the list of collector group names and retrieves collectors under the
given groups
            collectorGroupsIds: Specifies the list of collector group Ids and retrieves collectors under the
given groups
            collectorType: Specifies the group types of the collectors. Types: All, Collector, Workloads. All by default
            devices: Specifies the list of device names
            devicesIds: Specifies the list of device ids
            firstSeen: Retrieves collectors that were first seen after the value assigned to this date. Date Format: yyyy-MM-dd HH:mm:ss
            hasCrashDumps: Retrieves collectors that have crash dumps
            ips: Specifies the list of IP values
            itemsPerPage: An integer used for paging that indicates the number of collectors to retrieve forthe current page. The default is 100. The maximum value is 1,000
            lastSeenEnd: Retrieves collectors that were last seen before the value assigned to this date. Date Format: yyyy-MM-dd HH:mm:ss
            lastSeenStart: Retrieves collectors that were last seen after the value assigned to this date. Date Format: yyyy-MM-dd HH:mm:ss
            loggedUser: Specifies the user that was logged when the event occurred
            operatingSystems: Specifies the list of specific operating systems. For example, Windows 7 Pro
            osFamilies: Specifies the list of operating system families: Windows, Windows Server or OS X
            pageNumber: An integer used for paging that indicates the required page number
            releaseLicense: (Required) Collector releaseLicense
            showExpired: Specifies whether to include collectors which have been disconnected for more than 30 days (sequentially) and are marked as Expired
            sorting: Specifies a list of strings in JSON format representing the fields by which to sort the results in the following format: %7B"column1":true, "column2":false%7D. True indicates to sort in descending order.Results are sorted by the first field, then by the second field and so on
            states: Specifies the list of collector states: Running, Disconnected, Disabled, Degraded, 
Pending Reboot, Isolated, Expired, Migrated or Pending Migration
            strictMode: A true/false parameter indicating whether to perform strict matching on the search parameters. The default is False
            versions: Specifies the list of collector versions
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
            "/management-rest/inventory/release-license",
            params={
            "cloudAccounts": cloudAccounts,
            "cloudProviders": cloudProviders,
            "clusters": clusters,
            "collectorGroups": collectorGroups,
            "collectorGroupsIds": collectorGroupsIds,
            "collectorType": collectorType,
            "devices": devices,
            "devicesIds": devicesIds,
            "firstSeen": firstSeen,
            "hasCrashDumps": hasCrashDumps,
            "ips": ips,
            "itemsPerPage": itemsPerPage,
            "lastSeenEnd": lastSeenEnd,
            "lastSeenStart": lastSeenStart,
            "loggedUser": loggedUser,
            "operatingSystems": operatingSystems,
            "osFamilies": osFamilies,
            "pageNumber": pageNumber,
            "releaseLicense": releaseLicense,
            "showExpired": showExpired,
            "sorting": sorting,
            "states": states,
            "strictMode": strictMode,
            "versions": versions
        },
            organization=organization,
        )

    @mcp.tool(name="inventory_toggle_collectors")
    async def inventory_toggle_collectors(
        organization: str | None = None,
        cloudAccounts: str | None = None,
        cloudProviders: str | None = None,
        clusters: str | None = None,
        collectorGroups: str | None = None,
        collectorGroupsIds: int | None = None,
        collectorType: str | None = None,
        devices: str | None = None,
        devicesIds: int | None = None,
        enable: bool | None = None,
        firstSeen: str | None = None,
        hasCrashDumps: bool | None = None,
        ips: str | None = None,
        itemsPerPage: int | None = None,
        lastSeenEnd: str | None = None,
        lastSeenStart: str | None = None,
        loggedUser: str | None = None,
        operatingSystems: str | None = None,
        osFamilies: str | None = None,
        pageNumber: int | None = None,
        showExpired: bool | None = None,
        sorting: str | None = None,
        states: str | None = None,
        strictMode: bool | None = None,
        versions: str | None = None,
    ) -> Any:
        """This API call enables/disables a Collector(s). You must specify whether the Collector is to be enabled or disabled
        
        Endpoint: `PUT /management-rest/inventory/toggle-collectors`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            cloudAccounts: Specifies the list cloud account names
            cloudProviders: Specifies the list of cloud providers: AWS, Azure, GCP
            clusters: Specifies the list of cluster
            collectorGroups: Specifies the list of collector group names and retrieves collectors under the
given groups
            collectorGroupsIds: Specifies the list of collector group Ids and retrieves collectors under the
given groups
            collectorType: Specifies the group types of the collectors. Types: All, Collector, Workloads. All by default
            devices: Specifies the list of device names
            devicesIds: Specifies the list of device ids
            enable: (Required) Toggle enable
            firstSeen: Retrieves collectors that were first seen after the value assigned to this date. Date Format: yyyy-MM-dd HH:mm:ss
            hasCrashDumps: Retrieves collectors that have crash dumps
            ips: Specifies the list of IP values
            itemsPerPage: An integer used for paging that indicates the number of collectors to retrieve forthe current page. The default is 100. The maximum value is 1,000
            lastSeenEnd: Retrieves collectors that were last seen before the value assigned to this date. Date Format: yyyy-MM-dd HH:mm:ss
            lastSeenStart: Retrieves collectors that were last seen after the value assigned to this date. Date Format: yyyy-MM-dd HH:mm:ss
            loggedUser: Specifies the user that was logged when the event occurred
            operatingSystems: Specifies the list of specific operating systems. For example, Windows 7 Pro
            osFamilies: Specifies the list of operating system families: Windows, Windows Server or OS X
            pageNumber: An integer used for paging that indicates the required page number
            showExpired: Specifies whether to include collectors which have been disconnected for more than 30 days (sequentially) and are marked as Expired
            sorting: Specifies a list of strings in JSON format representing the fields by which to sort the results in the following format: %7B"column1":true, "column2":false%7D. True indicates to sort in descending order.Results are sorted by the first field, then by the second field and so on
            states: Specifies the list of collector states: Running, Disconnected, Disabled, Degraded, 
Pending Reboot, Isolated, Expired, Migrated or Pending Migration
            strictMode: A true/false parameter indicating whether to perform strict matching on the search parameters. The default is False
            versions: Specifies the list of collector versions
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
            "/management-rest/inventory/toggle-collectors",
            params={
            "cloudAccounts": cloudAccounts,
            "cloudProviders": cloudProviders,
            "clusters": clusters,
            "collectorGroups": collectorGroups,
            "collectorGroupsIds": collectorGroupsIds,
            "collectorType": collectorType,
            "devices": devices,
            "devicesIds": devicesIds,
            "enable": enable,
            "firstSeen": firstSeen,
            "hasCrashDumps": hasCrashDumps,
            "ips": ips,
            "itemsPerPage": itemsPerPage,
            "lastSeenEnd": lastSeenEnd,
            "lastSeenStart": lastSeenStart,
            "loggedUser": loggedUser,
            "operatingSystems": operatingSystems,
            "osFamilies": osFamilies,
            "pageNumber": pageNumber,
            "showExpired": showExpired,
            "sorting": sorting,
            "states": states,
            "strictMode": strictMode,
            "versions": versions
        },
            organization=organization,
        )

    @mcp.tool(name="inventory_uninstall_collectors")
    async def inventory_uninstall_collectors(
        organization: str | None = None,
        collectorIDs: int | None = None,
        collectorSIDs: str | None = None,
    ) -> Any:
        """This API uninstall collectors
        
        Endpoint: `POST /management-rest/inventory/uninstall-collectors`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            collectorIDs: Specifies the list of device ids
            collectorSIDs: Specifies the list of device machine SID
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
            "/management-rest/inventory/uninstall-collectors",
            params={
            "collectorIDs": collectorIDs,
            "collectorSIDs": collectorSIDs
        },
            organization=organization,
        )

    @mcp.tool(name="inventory_unisolate_collectors")
    async def inventory_unisolate_collectors(
        organization: str | None = None,
        devices: str | None = None,
        devicesIds: int | None = None,
    ) -> Any:
        """This API call isolate collector functionality
        
        Endpoint: `PUT /management-rest/inventory/unisolate-collectors`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            devices: Specifies the list of device names
            devicesIds: Specifies the list of device ids
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
            "/management-rest/inventory/unisolate-collectors",
            params={
            "devices": devices,
            "devicesIds": devicesIds
        },
            organization=organization,
        )

