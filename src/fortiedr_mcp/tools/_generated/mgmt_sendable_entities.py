"""Auto-generated tool stubs from FortiEDR Postman collection.

THIS FILE IS AUTO-GENERATED — DO NOT EDIT BY HAND.
To regenerate: python tools/gen_tools.py

Category: management-rest/sendable-entities
Endpoint count: 2
"""
from __future__ import annotations

from typing import Any

from mcp.server.fastmcp import FastMCP

from ...auth import AuthManager
from ...client import FortiEDRClient



def register_write(mcp: FastMCP, auth: AuthManager) -> None:
    @mcp.tool(name="sendable_entities_set_mail_format")
    async def sendable_entities_set_mail_format(
        organization: str | None = None,
        format: str | None = None,
    ) -> Any:
        """set mail format
        
        Endpoint: `PUT /management-rest/sendable-entities/set-mail-format`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            format: (Required) Specifies email format type
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
            "/management-rest/sendable-entities/set-mail-format",
            params={
            "format": format
        },
            organization=organization,
        )

    @mcp.tool(name="sendable_entities_syslog")
    async def sendable_entities_syslog(
        organization: str | None = None,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """This API creates syslog
        
        Endpoint: `POST /management-rest/sendable-entities/syslog`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            body: Request body (JSON). Expected fields: host, name, organization, port, protocol, syslogFormat, syslogRFCFormat, certificateBlob, fazDevId, privateKeyFile, privateKeyPassword, useClientCertificate, useSSL.
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
            "/management-rest/sendable-entities/syslog",
            params=None,
            json_body=body,
            organization=organization,
        )

