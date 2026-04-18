"""Auto-generated tool stubs from FortiEDR Postman collection.

THIS FILE IS AUTO-GENERATED — DO NOT EDIT BY HAND.
To regenerate: python tools/gen_tools.py

Category: management-rest/users
Endpoint count: 8
"""
from __future__ import annotations

from typing import Any

from mcp.server.fastmcp import FastMCP

from ...auth import AuthManager
from ...client import FortiEDRClient



def register_read(mcp: FastMCP, auth: AuthManager) -> None:
    @mcp.tool(name="users_get_sp_metadata")
    async def users_get_sp_metadata(
        organization: str | None = None,
    ) -> Any:
        """This API call retrieve the FortiEdr metadata by organization
        
        Endpoint: `GET /management-rest/users/get-sp-metadata`
        
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
            "/management-rest/users/get-sp-metadata",
            params=None,
            organization=organization,
        )

    @mcp.tool(name="users_list_users")
    async def users_list_users(
        organization: str | None = None,
    ) -> Any:
        """This API call outputs a list of the users in the system. Use the input parameters to filter the list
        
        Endpoint: `GET /management-rest/users/list-users`
        
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
            "/management-rest/users/list-users",
            params=None,
            organization=organization,
        )


def register_write(mcp: FastMCP, auth: AuthManager) -> None:
    @mcp.tool(name="users_create_user")
    async def users_create_user(
        organization: str | None = None,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """This API create user in the system. (only for Admin role
        
        Endpoint: `POST /management-rest/users/create-user`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            body: Request body (JSON). Expected fields: confirmPassword, email, firstName, lastName, password, role, username, customScript, remoteShell, restApi, title.
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
            "/management-rest/users/create-user",
            params=None,
            json_body=body,
            organization=organization,
        )

    @mcp.tool(name="users_reset_password")
    async def users_reset_password(
        organization: str | None = None,
        username: str | None = None,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """This API reset user password. Use the input parameters to filter organization
        
        Endpoint: `PUT /management-rest/users/reset-password`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            username: (Required) Specifies the name of the user
            body: Request body (JSON). Expected fields: confirmPassword, password.
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
            "/management-rest/users/reset-password",
            params={
            "username": username
        },
            json_body=body,
            organization=organization,
        )

    @mcp.tool(name="users_update_saml_settings")
    async def users_update_saml_settings(
        organization: str | None = None,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Create / Update SAML authentication settings per organization
        
        Endpoint: `POST /management-rest/users/update-saml-settings`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            body: formdata fields as a dict.
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
            "/management-rest/users/update-saml-settings",
            params=None,
            json_body=body,
            organization=organization,
        )

    @mcp.tool(name="users_update_user")
    async def users_update_user(
        organization: str | None = None,
        username: str | None = None,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """This API update user in the system. Use the input parameters to filter organization
        
        Endpoint: `PUT /management-rest/users/update-user`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            username: (Required) Specifies the name of the user
            body: Request body (JSON). Expected fields: email, firstName, lastName, role, username, customScript, remoteShell, restApi, title.
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
            "/management-rest/users/update-user",
            params={
            "username": username
        },
            json_body=body,
            organization=organization,
        )


def register_destructive(mcp: FastMCP, auth: AuthManager) -> None:
    @mcp.tool(name="users_delete_saml_settings")
    async def users_delete_saml_settings(
        organization: str | None = None,
        organizationNameRequest: str | None = None,
    ) -> Any:
        """Delete SAML authentication settings per organization
        
        Endpoint: `DELETE /management-rest/users/delete-saml-settings`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            organizationNameRequest: (Required) organizationNameRequest
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
            "/management-rest/users/delete-saml-settings",
            params={
            "organizationNameRequest": organizationNameRequest
        },
            organization=organization,
        )

    @mcp.tool(name="users_delete_user")
    async def users_delete_user(
        organization: str | None = None,
        username: str | None = None,
    ) -> Any:
        """This API delete user from the system. Use the input parameters to filter organization
        
        Endpoint: `DELETE /management-rest/users/delete-user`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            username: (Required) Specifies the name of the user
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
            "/management-rest/users/delete-user",
            params={
            "username": username
        },
            organization=organization,
        )

