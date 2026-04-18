"""Auto-generated tool stubs from FortiEDR Postman collection.

THIS FILE IS AUTO-GENERATED — DO NOT EDIT BY HAND.
To regenerate: python tools/gen_tools.py

Category: management-rest/integrations
Endpoint count: 6
"""
from __future__ import annotations

from typing import Any

from mcp.server.fastmcp import FastMCP

from ...auth import AuthManager
from ...client import FortiEDRClient



def register_read(mcp: FastMCP, auth: AuthManager) -> None:
    @mcp.tool(name="integrations_connectors_metadata")
    async def integrations_connectors_metadata(
        organization: str | None = None,
    ) -> Any:
        """Get connectors metadata, describing the valid values for connector fields definition and on-premise cores.
        
        Endpoint: `GET /management-rest/integrations/connectors-metadata`
        
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
            "/management-rest/integrations/connectors-metadata",
            params=None,
            organization=organization,
        )

    @mcp.tool(name="integrations_list_connectors")
    async def integrations_list_connectors(
        organization: str | None = None,
        onlyValidConnectors: bool | None = None,
    ) -> Any:
        """List all organization connectors
        
        Endpoint: `GET /management-rest/integrations/list-connectors`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            onlyValidConnectors: Set to true to retrieve enabled, non-failing connectors.
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
            "/management-rest/integrations/list-connectors",
            params={
            "onlyValidConnectors": onlyValidConnectors
        },
            organization=organization,
        )

    @mcp.tool(name="integrations_test_connector")
    async def integrations_test_connector(
        organization: str | None = None,
        connectorName: str | None = None,
        connectorType: str | None = None,
    ) -> Any:
        """Tests a connector
        
        Endpoint: `GET /management-rest/integrations/test-connector`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            connectorName: (Required) Specifies the connector's name (case sensitive)
            connectorType: (Required) Specifies the connector's type.
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
            "/management-rest/integrations/test-connector",
            params={
            "connectorName": connectorName,
            "connectorType": connectorType
        },
            organization=organization,
        )


def register_write(mcp: FastMCP, auth: AuthManager) -> None:
    @mcp.tool(name="integrations_create_connector")
    async def integrations_create_connector(
        organization: str | None = None,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Creates a new connector. Please note: Creation of Custom connectors/actions is not yet support.
        
        Endpoint: `POST /management-rest/integrations/create-connector`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            body: Request body (JSON). Expected fields: connectorActions, enabled, host, name, organization, port, type, vendor, apiKey, coreId, password, username.
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
            "/management-rest/integrations/create-connector",
            params=None,
            json_body=body,
            organization=organization,
        )

    @mcp.tool(name="integrations_update_connector")
    async def integrations_update_connector(
        organization: str | None = None,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Updates an existing connector based on (name, type, organization). Please note: Modification of Custom connectors/actions is not yet support.
        
        Endpoint: `PUT /management-rest/integrations/update-connector`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            body: Request body (JSON). Expected fields: connectorActions, enabled, host, name, organization, port, type, vendor, apiKey, coreId, password, username.
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
            "/management-rest/integrations/update-connector",
            params=None,
            json_body=body,
            organization=organization,
        )


def register_destructive(mcp: FastMCP, auth: AuthManager) -> None:
    @mcp.tool(name="integrations_delete_connector")
    async def integrations_delete_connector(
        organization: str | None = None,
        connectorName: str | None = None,
        connectorType: str | None = None,
    ) -> Any:
        """Deletes a connector
        
        Endpoint: `DELETE /management-rest/integrations/delete-connector`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            connectorName: (Required) Specifies the connector's name (case sensitive)
            connectorType: (Required) Specifies the connector's type.
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
            "/management-rest/integrations/delete-connector",
            params={
            "connectorName": connectorName,
            "connectorType": connectorType
        },
            organization=organization,
        )

