"""Auto-generated tool stubs from FortiEDR Postman collection.

THIS FILE IS AUTO-GENERATED — DO NOT EDIT BY HAND.
To regenerate: python tools/gen_tools.py

Category: management-rest/events
Endpoint count: 7
"""
from __future__ import annotations

from typing import Any

from mcp.server.fastmcp import FastMCP

from ...auth import AuthManager
from ...client import FortiEDRClient



def register_read(mcp: FastMCP, auth: AuthManager) -> None:
    @mcp.tool(name="events_count_events")
    async def events_count_events(
        organization: str | None = None,
        actions: str | None = None,
        applicationControl: bool | None = None,
        archived: bool | None = None,
        classifications: str | None = None,
        collectorGroups: str | None = None,
        collectorIds: int | None = None,
        destinations: str | None = None,
        device: str | None = None,
        deviceControl: bool | None = None,
        deviceIps: str | None = None,
        eventIds: int | None = None,
        eventType: str | None = None,
        expired: bool | None = None,
        fileHash: str | None = None,
        firstSeen: str | None = None,
        firstSeenFrom: str | None = None,
        firstSeenTo: str | None = None,
        handled: bool | None = None,
        itemsPerPage: int | None = None,
        lastSeen: str | None = None,
        lastSeenFrom: str | None = None,
        lastSeenTo: str | None = None,
        loggedUser: str | None = None,
        macAddresses: str | None = None,
        muted: bool | None = None,
        operatingSystems: str | None = None,
        pageNumber: int | None = None,
        paths: str | None = None,
        process: str | None = None,
        rule: str | None = None,
        seen: bool | None = None,
        severities: str | None = None,
        signed: bool | None = None,
        sorting: str | None = None,
        strictMode: bool | None = None,
    ) -> Any:
        """Count Events
        
        Endpoint: `GET /management-rest/events/count-events`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            actions: Specifies the action of the event
            applicationControl: A true/false parameter indicating whether to include only application control events
            archived: A true/false parameter indicating whether to include only archived events
            classifications: Specifies the classification of the event
            collectorGroups: Specifies the collector groups whose collector reported the events
            collectorIds: Specifies the collectorIds where the events occurred
            destinations: Specifies the connection destination(s) of the events
            device: Specifies the device name where the events occurred
            deviceControl: A true/false parameter indicating whether to include only device control events
            deviceIps: Specifies the IPs of the devices where the event occurred
            eventIds: Specifies the required event IDs
            eventType: Specifies the type of the event
            expired: A true/false parameter indicating whether to include only expired events
            fileHash: Specifies the hash signature of the main process of the event
            firstSeen: Specifies the date when the event was first seen (Deprecated)
            firstSeenFrom: Specifies the from date when the event was first seen
            firstSeenTo: Specifies the to date when the event was first seen
            handled: A true/false parameter indicating whether events were handled/unhandled
            itemsPerPage: An integer used for paging that indicates the number of collectors to retrieve forthe current page. The default is 100. The maximum value is 1,000
            lastSeen: Specifies the date when the event was last seen (Deprecated)
            lastSeenFrom: Specifies the from date when the event was last seen
            lastSeenTo: Specifies the to date when the event was last seen
            loggedUser: Specifies the logged user
            macAddresses: Specifies the mac addresses where the event occurred
            muted: A true/false parameter indicating if the event is muted
            operatingSystems: Specifies the operating system of the devices where the events occurred
            pageNumber: An integer used for paging that indicates the required page number
            paths: Specifies the paths of the processes related to the event
            process: Specifies the main process of the event
            rule: Specifies the short rule name of the rule that triggered the events
            seen: A true/false parameter indicating whether events were read/unread by the user operating the API
            severities: Specifies the severity of the event (Deprecated)
            signed: A true/false parameter indicating if the event is signed
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
            "/management-rest/events/count-events",
            params={
            "actions": actions,
            "applicationControl": applicationControl,
            "archived": archived,
            "classifications": classifications,
            "collectorGroups": collectorGroups,
            "collectorIds": collectorIds,
            "destinations": destinations,
            "device": device,
            "deviceControl": deviceControl,
            "deviceIps": deviceIps,
            "eventIds": eventIds,
            "eventType": eventType,
            "expired": expired,
            "fileHash": fileHash,
            "firstSeen": firstSeen,
            "firstSeenFrom": firstSeenFrom,
            "firstSeenTo": firstSeenTo,
            "handled": handled,
            "itemsPerPage": itemsPerPage,
            "lastSeen": lastSeen,
            "lastSeenFrom": lastSeenFrom,
            "lastSeenTo": lastSeenTo,
            "loggedUser": loggedUser,
            "macAddresses": macAddresses,
            "muted": muted,
            "operatingSystems": operatingSystems,
            "pageNumber": pageNumber,
            "paths": paths,
            "process": process,
            "rule": rule,
            "seen": seen,
            "severities": severities,
            "signed": signed,
            "sorting": sorting,
            "strictMode": strictMode
        },
            organization=organization,
        )

    @mcp.tool(name="events_export_raw_data_items_json")
    async def events_export_raw_data_items_json(
        organization: str | None = None,
        rawItemIds: str | None = None,
    ) -> Any:
        """Get event as Json format
        
        Endpoint: `GET /management-rest/events/export-raw-data-items-json`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            rawItemIds: Specifies the raw data item event IDs
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
            "/management-rest/events/export-raw-data-items-json",
            params={
            "rawItemIds": rawItemIds
        },
            organization=organization,
        )

    @mcp.tool(name="events_list_events")
    async def events_list_events(
        organization: str | None = None,
        actions: str | None = None,
        applicationControl: bool | None = None,
        archived: bool | None = None,
        classifications: str | None = None,
        collectorGroups: str | None = None,
        collectorIds: int | None = None,
        destinations: str | None = None,
        device: str | None = None,
        deviceControl: bool | None = None,
        deviceIps: str | None = None,
        eventIds: int | None = None,
        eventType: str | None = None,
        expired: bool | None = None,
        fileHash: str | None = None,
        firstSeen: str | None = None,
        firstSeenFrom: str | None = None,
        firstSeenTo: str | None = None,
        handled: bool | None = None,
        itemsPerPage: int | None = None,
        lastSeen: str | None = None,
        lastSeenFrom: str | None = None,
        lastSeenTo: str | None = None,
        loggedUser: str | None = None,
        macAddresses: str | None = None,
        muted: bool | None = None,
        operatingSystems: str | None = None,
        pageNumber: int | None = None,
        paths: str | None = None,
        process: str | None = None,
        rule: str | None = None,
        seen: bool | None = None,
        severities: str | None = None,
        signed: bool | None = None,
        sorting: str | None = None,
        strictMode: bool | None = None,
        allCollectorGroups: bool | None = None,
        allDestinations: bool | None = None,
        allUsers: bool | None = None,
        forceCreate: bool | None = None,
        comment: str | None = None,
        eventId: int | None = None,
    ) -> Any:
        """List Events
        
        Endpoint: `GET /management-rest/events/list-events`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            actions: Specifies the action of the event
            applicationControl: A true/false parameter indicating whether to include only application control events
            archived: A true/false parameter indicating whether to include only archived events
            classifications: Specifies the classification of the event
            collectorGroups: Specifies the collector groups whose collector reported the events
            collectorIds: Specifies the collectorIds where the events occurred
            destinations: Specifies the connection destination(s) of the events
            device: Specifies the device name where the events occurred
            deviceControl: A true/false parameter indicating whether to include only device control events
            deviceIps: Specifies the IPs of the devices where the event occurred
            eventIds: Specifies the required event IDs
            eventType: Specifies the type of the event
            expired: A true/false parameter indicating whether to include only expired events
            fileHash: Specifies the hash signature of the main process of the event
            firstSeen: Specifies the date when the event was first seen (Deprecated)
            firstSeenFrom: Specifies the from date when the event was first seen
            firstSeenTo: Specifies the to date when the event was first seen
            handled: A true/false parameter indicating whether events were handled/unhandled
            itemsPerPage: An integer used for paging that indicates the number of collectors to retrieve forthe current page. The default is 100. The maximum value is 1,000
            lastSeen: Specifies the date when the event was last seen (Deprecated)
            lastSeenFrom: Specifies the from date when the event was last seen
            lastSeenTo: Specifies the to date when the event was last seen
            loggedUser: Specifies the logged user
            macAddresses: Specifies the mac addresses where the event occurred
            muted: A true/false parameter indicating if the event is muted
            operatingSystems: Specifies the operating system of the devices where the events occurred
            pageNumber: An integer used for paging that indicates the required page number
            paths: Specifies the paths of the processes related to the event
            process: Specifies the main process of the event
            rule: Specifies the short rule name of the rule that triggered the events
            seen: A true/false parameter indicating whether events were read/unread by the user operating the API
            severities: Specifies the severity of the event (Deprecated)
            signed: A true/false parameter indicating if the event is signed
            sorting: Specifies a list of strings in JSON format representing the fields by which to sort the results in the following format: %7B"column1":true, "column2":false%7D. True indicates to sort in descending order.Results are sorted by the first field, then by the second field and so on
            strictMode: A true/false parameter indicating whether to perform strict matching on the search parameters. The default is False
            allCollectorGroups: Query param: `allCollectorGroups`
            allDestinations: Query param: `allDestinations`
            allUsers: Query param: `allUsers`
            forceCreate: Query param: `forceCreate`
            comment: Query param: `comment`
            eventId: Query param: `eventId`
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
            "/management-rest/events/list-events",
            params={
            "actions": actions,
            "applicationControl": applicationControl,
            "archived": archived,
            "classifications": classifications,
            "collectorGroups": collectorGroups,
            "collectorIds": collectorIds,
            "destinations": destinations,
            "device": device,
            "deviceControl": deviceControl,
            "deviceIps": deviceIps,
            "eventIds": eventIds,
            "eventType": eventType,
            "expired": expired,
            "fileHash": fileHash,
            "firstSeen": firstSeen,
            "firstSeenFrom": firstSeenFrom,
            "firstSeenTo": firstSeenTo,
            "handled": handled,
            "itemsPerPage": itemsPerPage,
            "lastSeen": lastSeen,
            "lastSeenFrom": lastSeenFrom,
            "lastSeenTo": lastSeenTo,
            "loggedUser": loggedUser,
            "macAddresses": macAddresses,
            "muted": muted,
            "operatingSystems": operatingSystems,
            "pageNumber": pageNumber,
            "paths": paths,
            "process": process,
            "rule": rule,
            "seen": seen,
            "severities": severities,
            "signed": signed,
            "sorting": sorting,
            "strictMode": strictMode,
            "allCollectorGroups": allCollectorGroups,
            "allDestinations": allDestinations,
            "allUsers": allUsers,
            "forceCreate": forceCreate,
            "comment": comment,
            "eventId": eventId
        },
            organization=organization,
        )

    @mcp.tool(name="events_list_raw_data_items")
    async def events_list_raw_data_items(
        organization: str | None = None,
        collectorGroups: str | None = None,
        destinations: str | None = None,
        device: str | None = None,
        deviceIps: str | None = None,
        eventId: int | None = None,
        firstSeen: str | None = None,
        firstSeenFrom: str | None = None,
        firstSeenTo: str | None = None,
        fullDataRequested: bool | None = None,
        itemsPerPage: int | None = None,
        lastSeen: str | None = None,
        lastSeenFrom: str | None = None,
        lastSeenTo: str | None = None,
        loggedUser: str | None = None,
        pageNumber: int | None = None,
        rawEventIds: int | None = None,
        sorting: str | None = None,
        strictMode: bool | None = None,
    ) -> Any:
        """List raw data items
        
        Endpoint: `GET /management-rest/events/list-raw-data-items`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            collectorGroups: Specifies the collector groups whose collector reported the raw events
            destinations: Specifies the connection destination(s) of the events
            device: Specifies the name of the device where the raw event occurred
            deviceIps: Specifies the IPs of the devices where the event occurred
            eventId: (Required) Specifies the ID of the event that holds the raw data items
            firstSeen: Specifies the date when the raw data item was first seen (Deprecated)
            firstSeenFrom: Specifies the from date when the raw data item was first seen
            firstSeenTo: Specifies the to date when the raw data item was first seen
            fullDataRequested: A true/false parameter indicating whether to include the event internal information
            itemsPerPage: An integer used for paging that indicates the number of collectors to retrieve forthe current page. The default is 100. The maximum value is 1,000
            lastSeen: Specifies the date when the raw data item was last seen (Deprecated)
            lastSeenFrom: Specifies the from date when the raw data item was last seen
            lastSeenTo: Specifies the to date when the raw data item was last seen
            loggedUser: Specifies the logged user
            pageNumber: An integer used for paging that indicates the required page number
            rawEventIds: Specifies the list of raw data item event IDs
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
            "/management-rest/events/list-raw-data-items",
            params={
            "collectorGroups": collectorGroups,
            "destinations": destinations,
            "device": device,
            "deviceIps": deviceIps,
            "eventId": eventId,
            "firstSeen": firstSeen,
            "firstSeenFrom": firstSeenFrom,
            "firstSeenTo": firstSeenTo,
            "fullDataRequested": fullDataRequested,
            "itemsPerPage": itemsPerPage,
            "lastSeen": lastSeen,
            "lastSeenFrom": lastSeenFrom,
            "lastSeenTo": lastSeenTo,
            "loggedUser": loggedUser,
            "pageNumber": pageNumber,
            "rawEventIds": rawEventIds,
            "sorting": sorting,
            "strictMode": strictMode
        },
            organization=organization,
        )


def register_write(mcp: FastMCP, auth: AuthManager) -> None:
    @mcp.tool(name="events_create_exception")
    async def events_create_exception(
        organization: str | None = None,
        allCollectorGroups: bool | None = None,
        allDestinations: bool | None = None,
        allOrganizations: bool | None = None,
        allUsers: bool | None = None,
        collectorGroups: str | None = None,
        comment: str | None = None,
        destinations: str | None = None,
        eventId: int | None = None,
        exceptionId: int | None = None,
        forceCreate: bool | None = None,
        isHidden: bool | None = None,
        users: str | None = None,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """This API call adds an exception to a specific event. The output of this call is a message indicating whether the creation of the exception
        
        Endpoint: `POST /management-rest/events/create-exception`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            allCollectorGroups: A true/false parameter indicating whether the exception should be applied to all collector groups. When not used, all collector groups are selected
            allDestinations: A true/false parameter indicating whether the exception should be applied to all destinations. When not used, all destinations are selected
            allOrganizations: A true/false parameter indicating whether the exception should be applied to all the organizations (tenants). This parameter is only relevant in multi-tenancy environment. This parameter is only allowed for user with Hoster privilege (general admin)
            allUsers: A true/false parameter indicating whether the exception should be applied to all users. When not used, all users are selected
            collectorGroups: Specifies the list of all the collector groups to which the exception should be applied. When not used, all collector groups are selected
            comment: Specifies a user-defined string to attach to the exception
            destinations: A list of IPs to which the exception applies and/or the value all internal destinations
            eventId: Specifies the event ID on which to create the exception
            exceptionId: Specifies the exception ID to edit
            forceCreate: A true/false parameter indicating whether to create the exception, even if there are already exceptions that cover this given event
            isHidden: A true/false parameter indicating whether the event is hidden
            users: A list of users to which the exception
            body: Request body (JSON). Expected fields: useAnyPath, useCommandLine, useInException, wildcardFiles, wildcardPaths.
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
            "/management-rest/events/create-exception",
            params={
            "allCollectorGroups": allCollectorGroups,
            "allDestinations": allDestinations,
            "allOrganizations": allOrganizations,
            "allUsers": allUsers,
            "collectorGroups": collectorGroups,
            "comment": comment,
            "destinations": destinations,
            "eventId": eventId,
            "exceptionId": exceptionId,
            "forceCreate": forceCreate,
            "isHidden": isHidden,
            "users": users
        },
            json_body=body,
            organization=organization,
        )

    @mcp.tool(name="events")
    async def events(
        organization: str | None = None,
        actions: str | None = None,
        applicationControl: bool | None = None,
        archived: bool | None = None,
        classifications: str | None = None,
        collectorGroups: str | None = None,
        collectorIds: int | None = None,
        destinations: str | None = None,
        device: str | None = None,
        deviceControl: bool | None = None,
        deviceIps: str | None = None,
        eventIds: int | None = None,
        eventType: str | None = None,
        expired: bool | None = None,
        fileHash: str | None = None,
        firstSeen: str | None = None,
        firstSeenFrom: str | None = None,
        firstSeenTo: str | None = None,
        handled: bool | None = None,
        itemsPerPage: int | None = None,
        lastSeen: str | None = None,
        lastSeenFrom: str | None = None,
        lastSeenTo: str | None = None,
        loggedUser: str | None = None,
        macAddresses: str | None = None,
        muted: bool | None = None,
        operatingSystems: str | None = None,
        pageNumber: int | None = None,
        paths: str | None = None,
        process: str | None = None,
        rule: str | None = None,
        seen: bool | None = None,
        severities: str | None = None,
        signed: bool | None = None,
        sorting: str | None = None,
        strictMode: bool | None = None,
        eventId: int | None = None,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """This API call updates the read/unread, handled/unhandled or archived/unarchived state of an event. The output of this call is a message indicating whether the update succeeded or failed
        
        Endpoint: `PUT /management-rest/events`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            actions: Specifies the action of the event
            applicationControl: A true/false parameter indicating whether to include only application control events
            archived: A true/false parameter indicating whether to include only archived events
            classifications: Specifies the classification of the event
            collectorGroups: Specifies the collector groups whose collector reported the events
            collectorIds: Specifies the collectorIds where the events occurred
            destinations: Specifies the connection destination(s) of the events
            device: Specifies the device name where the events occurred
            deviceControl: A true/false parameter indicating whether to include only device control events
            deviceIps: Specifies the IPs of the devices where the event occurred
            eventIds: Specifies the required event IDs
            eventType: Specifies the type of the event
            expired: A true/false parameter indicating whether to include only expired events
            fileHash: Specifies the hash signature of the main process of the event
            firstSeen: Specifies the date when the event was first seen (Deprecated)
            firstSeenFrom: Specifies the from date when the event was first seen
            firstSeenTo: Specifies the to date when the event was first seen
            handled: A true/false parameter indicating whether events were handled/unhandled
            itemsPerPage: An integer used for paging that indicates the number of collectors to retrieve forthe current page. The default is 100. The maximum value is 1,000
            lastSeen: Specifies the date when the event was last seen (Deprecated)
            lastSeenFrom: Specifies the from date when the event was last seen
            lastSeenTo: Specifies the to date when the event was last seen
            loggedUser: Specifies the logged user
            macAddresses: Specifies the mac addresses where the event occurred
            muted: A true/false parameter indicating if the event is muted
            operatingSystems: Specifies the operating system of the devices where the events occurred
            pageNumber: An integer used for paging that indicates the required page number
            paths: Specifies the paths of the processes related to the event
            process: Specifies the main process of the event
            rule: Specifies the short rule name of the rule that triggered the events
            seen: A true/false parameter indicating whether events were read/unread by the user operating the API
            severities: Specifies the severity of the event (Deprecated)
            signed: A true/false parameter indicating if the event is signed
            sorting: Specifies a list of strings in JSON format representing the fields by which to sort the results in the following format: %7B"column1":true, "column2":false%7D. True indicates to sort in descending order.Results are sorted by the first field, then by the second field and so on
            strictMode: A true/false parameter indicating whether to perform strict matching on the search parameters. The default is False
            eventId: Query param: `eventId`
            body: Request body (JSON). Expected fields: archive, classification, comment, familyName, forceUnmute, handle, malwareType, mute, muteDuration, read, threatName.
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
            "/management-rest/events",
            params={
            "actions": actions,
            "applicationControl": applicationControl,
            "archived": archived,
            "classifications": classifications,
            "collectorGroups": collectorGroups,
            "collectorIds": collectorIds,
            "destinations": destinations,
            "device": device,
            "deviceControl": deviceControl,
            "deviceIps": deviceIps,
            "eventIds": eventIds,
            "eventType": eventType,
            "expired": expired,
            "fileHash": fileHash,
            "firstSeen": firstSeen,
            "firstSeenFrom": firstSeenFrom,
            "firstSeenTo": firstSeenTo,
            "handled": handled,
            "itemsPerPage": itemsPerPage,
            "lastSeen": lastSeen,
            "lastSeenFrom": lastSeenFrom,
            "lastSeenTo": lastSeenTo,
            "loggedUser": loggedUser,
            "macAddresses": macAddresses,
            "muted": muted,
            "operatingSystems": operatingSystems,
            "pageNumber": pageNumber,
            "paths": paths,
            "process": process,
            "rule": rule,
            "seen": seen,
            "severities": severities,
            "signed": signed,
            "sorting": sorting,
            "strictMode": strictMode,
            "eventId": eventId
        },
            json_body=body,
            organization=organization,
        )


def register_destructive(mcp: FastMCP, auth: AuthManager) -> None:
    @mcp.tool(name="events")
    async def events(
        organization: str | None = None,
        actions: str | None = None,
        applicationControl: bool | None = None,
        archived: bool | None = None,
        classifications: str | None = None,
        collectorGroups: str | None = None,
        collectorIds: int | None = None,
        deleteAll: bool | None = None,
        destinations: str | None = None,
        device: str | None = None,
        deviceControl: bool | None = None,
        deviceIps: str | None = None,
        eventIds: int | None = None,
        eventType: str | None = None,
        expired: bool | None = None,
        fileHash: str | None = None,
        firstSeen: str | None = None,
        firstSeenFrom: str | None = None,
        firstSeenTo: str | None = None,
        handled: bool | None = None,
        itemsPerPage: int | None = None,
        lastSeen: str | None = None,
        lastSeenFrom: str | None = None,
        lastSeenTo: str | None = None,
        loggedUser: str | None = None,
        macAddresses: str | None = None,
        muted: bool | None = None,
        operatingSystems: str | None = None,
        pageNumber: int | None = None,
        paths: str | None = None,
        process: str | None = None,
        rule: str | None = None,
        seen: bool | None = None,
        severities: str | None = None,
        signed: bool | None = None,
        sorting: str | None = None,
        strictMode: bool | None = None,
    ) -> Any:
        """This API call delete events
        
        Endpoint: `DELETE /management-rest/events`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            actions: Specifies the action of the event
            applicationControl: A true/false parameter indicating whether to include only application control events
            archived: A true/false parameter indicating whether to include only archived events
            classifications: Specifies the classification of the event
            collectorGroups: Specifies the collector groups whose collector reported the events
            collectorIds: Specifies the collectorIds where the events occurred
            deleteAll: A true/false parameter indicating if all events should be deleted
            destinations: Specifies the connection destination(s) of the events
            device: Specifies the device name where the events occurred
            deviceControl: A true/false parameter indicating whether to include only device control events
            deviceIps: Specifies the IPs of the devices where the event occurred
            eventIds: Specifies the required event IDs
            eventType: Specifies the type of the event
            expired: A true/false parameter indicating whether to include only expired events
            fileHash: Specifies the hash signature of the main process of the event
            firstSeen: Specifies the date when the event was first seen (Deprecated)
            firstSeenFrom: Specifies the from date when the event was first seen
            firstSeenTo: Specifies the to date when the event was first seen
            handled: A true/false parameter indicating whether events were handled/unhandled
            itemsPerPage: An integer used for paging that indicates the number of collectors to retrieve forthe current page. The default is 100. The maximum value is 1,000
            lastSeen: Specifies the date when the event was last seen (Deprecated)
            lastSeenFrom: Specifies the from date when the event was last seen
            lastSeenTo: Specifies the to date when the event was last seen
            loggedUser: Specifies the logged user
            macAddresses: Specifies the mac addresses where the event occurred
            muted: A true/false parameter indicating if the event is muted
            operatingSystems: Specifies the operating system of the devices where the events occurred
            pageNumber: An integer used for paging that indicates the required page number
            paths: Specifies the paths of the processes related to the event
            process: Specifies the main process of the event
            rule: Specifies the short rule name of the rule that triggered the events
            seen: A true/false parameter indicating whether events were read/unread by the user operating the API
            severities: Specifies the severity of the event (Deprecated)
            signed: A true/false parameter indicating if the event is signed
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
            return await client.delete(
            "/management-rest/events",
            params={
            "actions": actions,
            "applicationControl": applicationControl,
            "archived": archived,
            "classifications": classifications,
            "collectorGroups": collectorGroups,
            "collectorIds": collectorIds,
            "deleteAll": deleteAll,
            "destinations": destinations,
            "device": device,
            "deviceControl": deviceControl,
            "deviceIps": deviceIps,
            "eventIds": eventIds,
            "eventType": eventType,
            "expired": expired,
            "fileHash": fileHash,
            "firstSeen": firstSeen,
            "firstSeenFrom": firstSeenFrom,
            "firstSeenTo": firstSeenTo,
            "handled": handled,
            "itemsPerPage": itemsPerPage,
            "lastSeen": lastSeen,
            "lastSeenFrom": lastSeenFrom,
            "lastSeenTo": lastSeenTo,
            "loggedUser": loggedUser,
            "macAddresses": macAddresses,
            "muted": muted,
            "operatingSystems": operatingSystems,
            "pageNumber": pageNumber,
            "paths": paths,
            "process": process,
            "rule": rule,
            "seen": seen,
            "severities": severities,
            "signed": signed,
            "sorting": sorting,
            "strictMode": strictMode
        },
            organization=organization,
        )

