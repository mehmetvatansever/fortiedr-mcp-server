"""Auto-generated tool stubs from FortiEDR Postman collection.

THIS FILE IS AUTO-GENERATED — DO NOT EDIT BY HAND.
To regenerate: python tools/gen_tools.py

Category: management-rest/policies
Endpoint count: 7
"""
from __future__ import annotations

from typing import Any

from mcp.server.fastmcp import FastMCP

from ...auth import AuthManager
from ...client import FortiEDRClient



def register_read(mcp: FastMCP, auth: AuthManager) -> None:
    @mcp.tool(name="policies_list_policies")
    async def policies_list_policies(
        organization: str | None = None,
    ) -> Any:
        """List policies
        
        Endpoint: `GET /management-rest/policies/list-policies`
        
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
            "/management-rest/policies/list-policies",
            params=None,
            organization=organization,
        )


def register_write(mcp: FastMCP, auth: AuthManager) -> None:
    @mcp.tool(name="policies_assign_collector_group")
    async def policies_assign_collector_group(
        organization: str | None = None,
        collectorsGroupName: str | None = None,
        forceAssign: bool | None = None,
        policyName: str | None = None,
    ) -> Any:
        """Assign collector group to policy
        
        Endpoint: `PUT /management-rest/policies/assign-collector-group`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            collectorsGroupName: (Required) Specifies the list of collector group names
            forceAssign: Indicates whether to force the assignment even if the group is assigned to similar policies
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
            "/management-rest/policies/assign-collector-group",
            params={
            "collectorsGroupName": collectorsGroupName,
            "forceAssign": forceAssign,
            "policyName": policyName
        },
            organization=organization,
        )

    @mcp.tool(name="policies_clone")
    async def policies_clone(
        organization: str | None = None,
        newPolicyName: str | None = None,
        sourcePolicyName: str | None = None,
    ) -> Any:
        """clone policy
        
        Endpoint: `POST /management-rest/policies/clone`
        
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
            "/management-rest/policies/clone",
            params={
            "newPolicyName": newPolicyName,
            "sourcePolicyName": sourcePolicyName
        },
            organization=organization,
        )

    @mcp.tool(name="policies_scan_files")
    async def policies_scan_files(
        organization: str | None = None,
        applyRecursiveScan: bool | None = None,
        executableFilesOnly: bool | None = None,
        filePaths: str | None = None,
        origin: str | None = None,
        scanBy: str | None = None,
        scanSelection: str | None = None,
    ) -> Any:
        """Scan Files
        
        Endpoint: `POST /management-rest/policies/scan-files`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            applyRecursiveScan: (Required) Specifies if execution includes recursive scan
            executableFilesOnly: (Required) Specifies if execution includes only files
            filePaths: Specifies file path
            origin: (Required) Specifies scan origin
            scanBy: (Required) Specifies scan by choice
            scanSelection: Specifies scan selection
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
            "/management-rest/policies/scan-files",
            params={
            "applyRecursiveScan": applyRecursiveScan,
            "executableFilesOnly": executableFilesOnly,
            "filePaths": filePaths,
            "origin": origin,
            "scanBy": scanBy,
            "scanSelection": scanSelection
        },
            organization=organization,
        )

    @mcp.tool(name="policies_set_mode")
    async def policies_set_mode(
        organization: str | None = None,
        mode: str | None = None,
        policyName: str | None = None,
    ) -> Any:
        """Set policy to simulation/prevention
        
        Endpoint: `PUT /management-rest/policies/set-mode`
        
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
            "/management-rest/policies/set-mode",
            params={
            "mode": mode,
            "policyName": policyName
        },
            organization=organization,
        )

    @mcp.tool(name="policies_set_policy_rule_action")
    async def policies_set_policy_rule_action(
        organization: str | None = None,
        action: str | None = None,
        policyName: str | None = None,
        ruleName: str | None = None,
    ) -> Any:
        """Set rule in policy to block/log
        
        Endpoint: `PUT /management-rest/policies/set-policy-rule-action`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            action: (Required) Specifies the policy action
            policyName: (Required) Specifies security policy name
            ruleName: (Required) Specifies rule name
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
            "/management-rest/policies/set-policy-rule-action",
            params={
            "action": action,
            "policyName": policyName,
            "ruleName": ruleName
        },
            organization=organization,
        )

    @mcp.tool(name="policies_set_policy_rule_state")
    async def policies_set_policy_rule_state(
        organization: str | None = None,
        policyName: str | None = None,
        ruleName: str | None = None,
        state: str | None = None,
    ) -> Any:
        """Set rule in policy to enable/disable
        
        Endpoint: `PUT /management-rest/policies/set-policy-rule-state`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            policyName: (Required) Specifies security policy name
            ruleName: (Required) Specifies rule name
            state: (Required) Policy rule state
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
            "/management-rest/policies/set-policy-rule-state",
            params={
            "policyName": policyName,
            "ruleName": ruleName,
            "state": state
        },
            organization=organization,
        )

