"""Auto-generated tool stubs from FortiEDR Postman collection.

THIS FILE IS AUTO-GENERATED — DO NOT EDIT BY HAND.
To regenerate: python tools/gen_tools.py

Category: management-rest/exceptions
Endpoint count: 5
"""
from __future__ import annotations

from typing import Any

from mcp.server.fastmcp import FastMCP

from ...auth import AuthManager
from ...client import FortiEDRClient



def register_read(mcp: FastMCP, auth: AuthManager) -> None:
    @mcp.tool(name="exceptions_get_event_exceptions")
    async def exceptions_get_event_exceptions(
        organization: str | None = None,
        eventId: int | None = None,
    ) -> Any:
        """Show exceptions
        
        Endpoint: `GET /management-rest/exceptions/get-event-exceptions`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            eventId: (Required) Specifies the required event ID
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
            "/management-rest/exceptions/get-event-exceptions",
            params={
            "eventId": eventId
        },
            organization=organization,
        )

    @mcp.tool(name="exceptions_list_exceptions")
    async def exceptions_list_exceptions(
        organization: str | None = None,
        collectorGroups: str | None = None,
        comment: str | None = None,
        createdAfter: str | None = None,
        createdBefore: str | None = None,
        destination: str | None = None,
        exceptionIds: int | None = None,
        path: str | None = None,
        process: str | None = None,
        rules: str | None = None,
        updatedAfter: str | None = None,
        updatedBefore: str | None = None,
        user: str | None = None,
    ) -> Any:
        """List of exceptions
        
        Endpoint: `GET /management-rest/exceptions/list-exceptions`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            collectorGroups: Specifies the list of all the collector groups to which the exception applied
            comment: Specifies a comment attach to the exception
            createdAfter: Specifies the date after which the exception was created. Specify the date using the yyyy-MM-dd HH:mm:ss format
            createdBefore: Specifies the date before which the exception was created. Specify the date using the yyyy-MM-dd HH:mm:ss format
            destination: Specifies a destination IP of the exception
            exceptionIds: Specifies a list of exception ids
            path: Specifies the path of the exception
            process: Specifies the process of the exception
            rules: Specifies a list of rule names
            updatedAfter: Specifies the date after which the exception was updated. Specify the date using the yyyy-MM-dd HH:mm:ss format
            updatedBefore: Specifies the date before which the exception was updated. Specify the date using the yyyy-MM-dd HH:mm:ss format
            user: Specifies a user of the exception
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
            "/management-rest/exceptions/list-exceptions",
            params={
            "collectorGroups": collectorGroups,
            "comment": comment,
            "createdAfter": createdAfter,
            "createdBefore": createdBefore,
            "destination": destination,
            "exceptionIds": exceptionIds,
            "path": path,
            "process": process,
            "rules": rules,
            "updatedAfter": updatedAfter,
            "updatedBefore": updatedBefore,
            "user": user
        },
            organization=organization,
        )


def register_write(mcp: FastMCP, auth: AuthManager) -> None:
    @mcp.tool(name="exceptions_create_or_edit_exception")
    async def exceptions_create_or_edit_exception(
        organization: str | None = None,
        confirmEdit: bool | None = None,
    ) -> Any:
        """This API call creates a new exception or updates an existing exception based on the given exception JSON body parameter
        
        Endpoint: `POST /management-rest/exceptions/create-or-edit-exception`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            confirmEdit: Confirm editing an existing exception in case of providing an exception ID in the body JSON. By default confirmEdit is false
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
            "/management-rest/exceptions/create-or-edit-exception",
            params={
            "confirmEdit": confirmEdit
        },
            organization=organization,
        )

    @mcp.tool(name="exceptions_update_exceptions_to_all_accounts_groups_coverage")
    async def exceptions_update_exceptions_to_all_accounts_groups_coverage(
        organization: str | None = None,
    ) -> Any:
        """This API call set an exception to a 'All organizations agents groups'
        
        Endpoint: `POST /management-rest/exceptions/update-exceptions-to-all-accounts-groups-coverage`
        
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
            "/management-rest/exceptions/update-exceptions-to-all-accounts-groups-coverage",
            params=None,
            organization=organization,
        )


def register_destructive(mcp: FastMCP, auth: AuthManager) -> None:
    @mcp.tool(name="exceptions_delete")
    async def exceptions_delete(
        organization: str | None = None,
        collectorGroups: str | None = None,
        comment: str | None = None,
        createdAfter: str | None = None,
        createdBefore: str | None = None,
        deleteAll: bool | None = None,
        destination: str | None = None,
        exceptionId: int | None = None,
        exceptionIds: int | None = None,
        path: str | None = None,
        process: str | None = None,
        rules: str | None = None,
        updatedAfter: str | None = None,
        updatedBefore: str | None = None,
        user: str | None = None,
    ) -> Any:
        """Delete exceptions
        
        Endpoint: `DELETE /management-rest/exceptions/delete`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            collectorGroups: Specifies the list of all the collector groups to which the exception applied
            comment: Specifies a comment attach to the exception
            createdAfter: Specifies the date after which the exception was created. Specify the date using the yyyy-MM-dd HH:mm:ss format
            createdBefore: Specifies the date before which the exception was created. Specify the date using the yyyy-MM-dd HH:mm:ss format
            deleteAll: A true/false parameter indicating if all exception should be deleted
            destination: Specifies a destination IP of the exception
            exceptionId: Specifies the required exception ID
            exceptionIds: Specifies a list of exception ids
            path: Specifies the path of the exception
            process: Specifies the process of the exception
            rules: Specifies a list of rule names
            updatedAfter: Specifies the date after which the exception was updated. Specify the date using the yyyy-MM-dd HH:mm:ss format
            updatedBefore: Specifies the date before which the exception was updated. Specify the date using the yyyy-MM-dd HH:mm:ss format
            user: Specifies a user of the exception
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
            "/management-rest/exceptions/delete",
            params={
            "collectorGroups": collectorGroups,
            "comment": comment,
            "createdAfter": createdAfter,
            "createdBefore": createdBefore,
            "deleteAll": deleteAll,
            "destination": destination,
            "exceptionId": exceptionId,
            "exceptionIds": exceptionIds,
            "path": path,
            "process": process,
            "rules": rules,
            "updatedAfter": updatedAfter,
            "updatedBefore": updatedBefore,
            "user": user
        },
            organization=organization,
        )

