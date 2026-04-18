"""Auto-generated tool stubs from FortiEDR Postman collection.

THIS FILE IS AUTO-GENERATED — DO NOT EDIT BY HAND.
To regenerate: python tools/gen_tools.py

Category: management-rest/forensics
Endpoint count: 3
"""
from __future__ import annotations

from typing import Any

from mcp.server.fastmcp import FastMCP

from ...auth import AuthManager
from ...client import FortiEDRClient



def register_read(mcp: FastMCP, auth: AuthManager) -> None:
    @mcp.tool(name="forensics_get_event_file")
    async def forensics_get_event_file(
        organization: str | None = None,
        disk: bool | None = None,
        endRange: str | None = None,
        filePaths: str | None = None,
        memory: bool | None = None,
        processId: int | None = None,
        rawEventId: int | None = None,
        startRange: str | None = None,
    ) -> Any:
        """This API call retrieves a file or memory
        
        Endpoint: `GET /management-rest/forensics/get-event-file`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            disk: A true/false parameter indicating whether find in the disk
            endRange: Specifies the memory end range, in Hexadecimal format
            filePaths: Specifies the list of file paths
            memory: A true/false parameter indicating whether find in the memory
            processId: Specifies the ID of the process from which to take a memory image. required for memory base action
            rawEventId: (Required) Specifies the ID of the raw event on which to perform the memory retrieval
            startRange: Specifies the memory start range, in Hexadecimal format
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
            "/management-rest/forensics/get-event-file",
            params={
            "disk": disk,
            "endRange": endRange,
            "filePaths": filePaths,
            "memory": memory,
            "processId": processId,
            "rawEventId": rawEventId,
            "startRange": startRange
        },
            organization=organization,
        )

    @mcp.tool(name="forensics_get_file")
    async def forensics_get_file(
        organization: str | None = None,
        device: str | None = None,
        filePaths: str | None = None,
        type: str | None = None,
    ) -> Any:
        """This API call retrieves a file or memory
        
        Endpoint: `GET /management-rest/forensics/get-file`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            device: (Required) Specifies the name or id of the device to remediate
            filePaths: (Required) Specifies the list of file paths
            type: (Required) Specifies the device parameter type used in the request : Name or ID
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
            "/management-rest/forensics/get-file",
            params={
            "device": device,
            "filePaths": filePaths,
            "type": type
        },
            organization=organization,
        )


def register_destructive(mcp: FastMCP, auth: AuthManager) -> None:
    @mcp.tool(name="forensics_remediate_device")
    async def forensics_remediate_device(
        organization: str | None = None,
        device: str | None = None,
        deviceId: int | None = None,
        executablesToRemove: str | None = None,
        persistenceDataAction: str | None = None,
        persistenceDataNewContent: str | None = None,
        persistenceDataPath: str | None = None,
        persistenceDataValueName: str | None = None,
        persistenceDataValueNewType: str | None = None,
        processName: str | None = None,
        terminatedProcessId: int | None = None,
        threadId: int | None = None,
    ) -> Any:
        """This API kill process / delete file / clean persistence, File and persistence paths must be specified in a logical format
        
        Endpoint: `PUT /management-rest/forensics/remediate-device`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            device: Specifies the name of the device to remediate. You must specify a value for either device or deviceId (see below)
            deviceId: Specifies the unique identifier (ID) of the device to remediate. You must specify a value for either deviceId or device (see above)
            executablesToRemove: Specifies the list of full paths of executable files (*.exe) to delete on the
given device
            persistenceDataAction: persistence data desired action
            persistenceDataNewContent: persistence data new content
            persistenceDataPath: persistence data path
            persistenceDataValueName: persistence data value name
            persistenceDataValueNewType: persistence data value new type
            processName: Specifies the process name
            terminatedProcessId: (Required) Represents the process ID to terminate on the device
            threadId: Specifies the thread ID
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
            "/management-rest/forensics/remediate-device",
            params={
            "device": device,
            "deviceId": deviceId,
            "executablesToRemove": executablesToRemove,
            "persistenceDataAction": persistenceDataAction,
            "persistenceDataNewContent": persistenceDataNewContent,
            "persistenceDataPath": persistenceDataPath,
            "persistenceDataValueName": persistenceDataValueName,
            "persistenceDataValueNewType": persistenceDataValueNewType,
            "processName": processName,
            "terminatedProcessId": terminatedProcessId,
            "threadId": threadId
        },
            organization=organization,
        )

