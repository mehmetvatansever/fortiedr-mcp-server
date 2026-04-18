"""Auto-generated tool stubs from FortiEDR Postman collection.

THIS FILE IS AUTO-GENERATED — DO NOT EDIT BY HAND.
To regenerate: python tools/gen_tools.py

Category: management-rest/playbooks-policies
Endpoint count: 6
"""
from __future__ import annotations

from typing import Any

from mcp.server.fastmcp import FastMCP

from ...auth import AuthManager
from ...client import FortiEDRClient



def register_read(mcp: FastMCP, auth: AuthManager) -> None:
    @mcp.tool(name="playbooks_policies_list_policies")
    async def playbooks_policies_list_policies(
        organization: str | None = None,
    ) -> Any:
        """List policies
        
        Endpoint: `GET /management-rest/playbooks-policies/list-policies`
        
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
            "/management-rest/playbooks-policies/list-policies",
            params=None,
            organization=organization,
        )


def register_write(mcp: FastMCP, auth: AuthManager) -> None:
    @mcp.tool(name="playbooks_policies_assign_collector_group")
    async def playbooks_policies_assign_collector_group(
        organization: str | None = None,
        collectorGroupNames: str | None = None,
        forceAssign: bool | None = None,
        policyName: str | None = None,
    ) -> Any:
        """Assign collector group to air policy
        
        Endpoint: `PUT /management-rest/playbooks-policies/assign-collector-group`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            collectorGroupNames: (Required) Specifies the list of collector group names
            forceAssign: Indicates whether to force the assignment even if the group is assigned to similar policies
            policyName: (Required) Specifies policy name
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
            "/management-rest/playbooks-policies/assign-collector-group",
            params={
            "collectorGroupNames": collectorGroupNames,
            "forceAssign": forceAssign,
            "policyName": policyName
        },
            organization=organization,
        )

    @mcp.tool(name="playbooks_policies_clone")
    async def playbooks_policies_clone(
        organization: str | None = None,
        newPolicyName: str | None = None,
        sourcePolicyName: str | None = None,
    ) -> Any:
        """clone policy
        
        Endpoint: `POST /management-rest/playbooks-policies/clone`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            newPolicyName: (Required) Specifies security policy target name.
            sourcePolicyName: (Required) Specifies security policy source name
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
            "/management-rest/playbooks-policies/clone",
            params={
            "newPolicyName": newPolicyName,
            "sourcePolicyName": sourcePolicyName
        },
            organization=organization,
        )

    @mcp.tool(name="playbooks_policies_map_connectors_to_actions")
    async def playbooks_policies_map_connectors_to_actions(
        organization: str | None = None,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Assign policy actions with connectors.
        
        Endpoint: `PUT /management-rest/playbooks-policies/map-connectors-to-actions`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            body: Request body (JSON). Expected fields: policyName, customActionsToConnectorsMaps, fortinetActionsToConnectorsMaps.
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
            "/management-rest/playbooks-policies/map-connectors-to-actions",
            params=None,
            json_body=body,
            organization=organization,
        )

    @mcp.tool(name="playbooks_policies_set_action_classification")
    async def playbooks_policies_set_action_classification(
        organization: str | None = None,
        body: dict[str, Any] | None = None,
    ) -> Any:
        """Set the air policy actions' classifications.
        
        Endpoint: `PUT /management-rest/playbooks-policies/set-action-classification`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            body: Request body (JSON). Expected fields: policyName, customActionsToClassificationMaps, fortinetActionsToClassificationMaps.
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
            "/management-rest/playbooks-policies/set-action-classification",
            params=None,
            json_body=body,
            organization=organization,
        )

    @mcp.tool(name="playbooks_policies_set_mode")
    async def playbooks_policies_set_mode(
        organization: str | None = None,
        mode: str | None = None,
        policyName: str | None = None,
    ) -> Any:
        """Set playbook to simulation/prevention
        
        Endpoint: `PUT /management-rest/playbooks-policies/set-mode`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            mode: (Required) Operation mode
            policyName: (Required) Specifies security policy name
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
            "/management-rest/playbooks-policies/set-mode",
            params={
            "mode": mode,
            "policyName": policyName
        },
            organization=organization,
        )

