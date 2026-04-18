"""Auto-generated tool stubs from FortiEDR Postman collection.

THIS FILE IS AUTO-GENERATED — DO NOT EDIT BY HAND.
To regenerate: python tools/gen_tools.py

Category: management-rest/comm-control
Endpoint count: 8
"""
from __future__ import annotations

from typing import Any

from mcp.server.fastmcp import FastMCP

from ...auth import AuthManager
from ...client import FortiEDRClient



def register_read(mcp: FastMCP, auth: AuthManager) -> None:
    @mcp.tool(name="comm_control_list_policies")
    async def comm_control_list_policies(
        organization: str | None = None,
        decisions: str | None = None,
        itemsPerPage: int | None = None,
        pageNumber: int | None = None,
        policies: str | None = None,
        rules: str | None = None,
        sorting: str | None = None,
        sources: str | None = None,
        state: str | None = None,
        strictMode: bool | None = None,
    ) -> Any:
        """This API call outputs a list of all the communication control policies in the system, and information about each of them
        
        Endpoint: `GET /management-rest/comm-control/list-policies`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            decisions: (Required) Indicates the action
            itemsPerPage: An integer used for paging that indicates the number of collectors to retrieve forthe current page. The default is 100. The maximum value is 1,000
            pageNumber: An integer used for paging that indicates the required page number
            policies: Specifies the list of policy names
            rules: Specifies the list of rules
            sorting: Specifies a list of strings in JSON format representing the fields by which to sort the results in the following format: %7B"column1":true, "column2":false%7D. True indicates to sort in descending order.Results are sorted by the first field, then by the second field and so on
            sources: Specifies who created the policy
            state: Policy rule state
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
            "/management-rest/comm-control/list-policies",
            params={
            "decisions": decisions,
            "itemsPerPage": itemsPerPage,
            "pageNumber": pageNumber,
            "policies": policies,
            "rules": rules,
            "sorting": sorting,
            "sources": sources,
            "state": state,
            "strictMode": strictMode
        },
            organization=organization,
        )

    @mcp.tool(name="comm_control_list_products")
    async def comm_control_list_products(
        organization: str | None = None,
        action: str | None = None,
        collectorGroups: str | None = None,
        cveIdentifier: str | None = None,
        destinationIp: str | None = None,
        devices: str | None = None,
        firstConnectionTimeEnd: str | None = None,
        firstConnectionTimeStart: str | None = None,
        handled: bool | None = None,
        includeStatistics: bool | None = None,
        ips: str | None = None,
        itemsPerPage: int | None = None,
        lastConnectionTimeEnd: str | None = None,
        lastConnectionTimeStart: str | None = None,
        os: str | None = None,
        pageNumber: int | None = None,
        policies: str | None = None,
        processHash: str | None = None,
        processes: str | None = None,
        product: str | None = None,
        products: str | None = None,
        reputation: str | None = None,
        rule: str | None = None,
        rulePolicy: str | None = None,
        seen: bool | None = None,
        sorting: str | None = None,
        strictMode: bool | None = None,
        vendor: str | None = None,
        vendors: str | None = None,
        version: str | None = None,
        versions: str | None = None,
        vulnerabilities: str | None = None,
    ) -> Any:
        """This API call outputs a list of all the communicating applications in the system, and information about each of them
        
        Endpoint: `GET /management-rest/comm-control/list-products`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            action: Indicates the action: Allow/Deny. This parameter is irrelevant without policies parameter
            collectorGroups: Specifies the list of collector groups where the products were seen
            cveIdentifier: Specifies the CVE identifier
            destinationIp: Destination IPs
            devices: Specifies the list of device names where the products were seen
            firstConnectionTimeEnd: Retrieves products whose first connection time is less than the value assigned to this date
            firstConnectionTimeStart: Retrieves products whose first connection time is greater than the value assigned to this date
            handled: A true/false parameter indicating whether events were handled/unhandled
            includeStatistics: A true/false parameter indicating including statistics data
            ips: Specifies the list of IPs where the products were seen
            itemsPerPage: An integer used for paging that indicates the number of collectors to retrieve forthe current page. The default is 100. The maximum value is 1,000
            lastConnectionTimeEnd: Retrieves products whose last connection time is less than the value assigned to this date
            lastConnectionTimeStart: Retrieves products whose last connection time is greater than the value assigned to this date
            os: Specifies the list of operating system families where the products were seen
            pageNumber: An integer used for paging that indicates the required page number
            policies: Specifies the list of policy names whose products have a specific decision, as specified in the action parameter
            processHash: Specifies the process hash name
            processes: Specifies the list of process names running alongside the products
            product: Specifies a single value for the product name. By default, strictMode is false
            products: Specifies the list of product names. Names must match exactly (strictMode is always true)
            reputation: Specifies the recommendation of the application: Unknown, Known bad, Assumed bad, Contradiction, Assumed good or Known good
            rule: Indicates the rule. This parameter is irrelevant without rulePolicy parameter
            rulePolicy: Specifies the policy name whose products have a specific rule, as specified in the rule parameter
            seen: A true/false parameter indicating whether events were read/unread by the user operating the API
            sorting: Specifies a list of strings in JSON format representing the fields by which to sort the results in the following format: %7B"column1":true, "column2":false%7D. True indicates to sort in descending order.Results are sorted by the first field, then by the second field and so on
            strictMode: A true/false parameter indicating whether to perform strict matching on the search parameters. The default is False
            vendor: Specifies a single value for the vendor name. By default, strictMode is false
            vendors: Specifies the list of vendor names. Names must match exactly (strictMode is always true)
            version: Specifies a single value for the version name. By default, strictMode is false
            versions: Specifies the list of versions. Names must match exactly (strictMode is always true)
            vulnerabilities: Specifies the list of vulnerabilities where the products were seen
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
            "/management-rest/comm-control/list-products",
            params={
            "action": action,
            "collectorGroups": collectorGroups,
            "cveIdentifier": cveIdentifier,
            "destinationIp": destinationIp,
            "devices": devices,
            "firstConnectionTimeEnd": firstConnectionTimeEnd,
            "firstConnectionTimeStart": firstConnectionTimeStart,
            "handled": handled,
            "includeStatistics": includeStatistics,
            "ips": ips,
            "itemsPerPage": itemsPerPage,
            "lastConnectionTimeEnd": lastConnectionTimeEnd,
            "lastConnectionTimeStart": lastConnectionTimeStart,
            "os": os,
            "pageNumber": pageNumber,
            "policies": policies,
            "processHash": processHash,
            "processes": processes,
            "product": product,
            "products": products,
            "reputation": reputation,
            "rule": rule,
            "rulePolicy": rulePolicy,
            "seen": seen,
            "sorting": sorting,
            "strictMode": strictMode,
            "vendor": vendor,
            "vendors": vendors,
            "version": version,
            "versions": versions,
            "vulnerabilities": vulnerabilities
        },
            organization=organization,
        )


def register_write(mcp: FastMCP, auth: AuthManager) -> None:
    @mcp.tool(name="comm_control_assign_collector_group")
    async def comm_control_assign_collector_group(
        organization: str | None = None,
        collectorGroups: str | None = None,
        forceAssign: bool | None = None,
        policyName: str | None = None,
    ) -> Any:
        """Assign collector group to application policy
        
        Endpoint: `PUT /management-rest/comm-control/assign-collector-group`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            collectorGroups: (Required)  Specifies the collector groups whose collector reported the events
            forceAssign: Indicates whether to force the assignment even if the group is assigned to similar policies
            policyName: (Required) Specifies the list of policies
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
            "/management-rest/comm-control/assign-collector-group",
            params={
            "collectorGroups": collectorGroups,
            "forceAssign": forceAssign,
            "policyName": policyName
        },
            organization=organization,
        )

    @mcp.tool(name="comm_control_clone_policy")
    async def comm_control_clone_policy(
        organization: str | None = None,
        newPolicyName: str | None = None,
        sourcePolicyName: str | None = None,
    ) -> Any:
        """application clone policy
        
        Endpoint: `POST /management-rest/comm-control/clone-policy`
        
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
            "/management-rest/comm-control/clone-policy",
            params={
            "newPolicyName": newPolicyName,
            "sourcePolicyName": sourcePolicyName
        },
            organization=organization,
        )

    @mcp.tool(name="comm_control_resolve_applications")
    async def comm_control_resolve_applications(
        organization: str | None = None,
        applyNested: bool | None = None,
        comment: str | None = None,
        products: str | None = None,
        resolve: bool | None = None,
        signed: bool | None = None,
        vendors: str | None = None,
        versions: str | None = None,
    ) -> Any:
        """Enable resolving/unresolving applications
        
        Endpoint: `PUT /management-rest/comm-control/resolve-applications`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            applyNested: A true/false parameter indicating updating inherited
            comment: Specifies a user-defined string to attach to the policy
            products: Specifies the list of product names. Names must match exactly (strictMode is always true)
            resolve: A true/false parameter indicating update the application resolve/unresolve
            signed: A true/false parameter indicating if the policy is signed
            vendors: Specifies the list of vendor names. Names must match exactly (strictMode is always true)
            versions: Specifies the list of versions. Names must match exactly (strictMode is always true)
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
            "/management-rest/comm-control/resolve-applications",
            params={
            "applyNested": applyNested,
            "comment": comment,
            "products": products,
            "resolve": resolve,
            "signed": signed,
            "vendors": vendors,
            "versions": versions
        },
            organization=organization,
        )

    @mcp.tool(name="comm_control_set_policy_mode")
    async def comm_control_set_policy_mode(
        organization: str | None = None,
        mode: str | None = None,
        policyNames: str | None = None,
    ) -> Any:
        """Set policy to simulation/prevention
        
        Endpoint: `PUT /management-rest/comm-control/set-policy-mode`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            mode: (Required) Operation mode
            policyNames: (Required) Specifies the list of policies
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
            "/management-rest/comm-control/set-policy-mode",
            params={
            "mode": mode,
            "policyNames": policyNames
        },
            organization=organization,
        )

    @mcp.tool(name="comm_control_set_policy_permission")
    async def comm_control_set_policy_permission(
        organization: str | None = None,
        applyNested: bool | None = None,
        decision: str | None = None,
        policies: str | None = None,
        products: str | None = None,
        signed: bool | None = None,
        vendors: str | None = None,
        versions: str | None = None,
    ) -> Any:
        """Set the application allow/deny
        
        Endpoint: `PUT /management-rest/comm-control/set-policy-permission`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            applyNested: A true/false parameter indicating updating inherited
            decision: (Required) Indicates the action
            policies: (Required) Specifies the list of policies names
            products: Specifies the list of product names. Names must match exactly (strictMode is always true)
            signed: A true/false parameter indicating if the policy is signed
            vendors: Specifies the list of vendor names. Names must match exactly (strictMode is always true)
            versions: Specifies the list of versions. Names must match exactly (strictMode is always true)
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
            "/management-rest/comm-control/set-policy-permission",
            params={
            "applyNested": applyNested,
            "decision": decision,
            "policies": policies,
            "products": products,
            "signed": signed,
            "vendors": vendors,
            "versions": versions
        },
            organization=organization,
        )

    @mcp.tool(name="comm_control_set_policy_rule_state")
    async def comm_control_set_policy_rule_state(
        organization: str | None = None,
        policyName: str | None = None,
        ruleName: str | None = None,
        state: str | None = None,
    ) -> Any:
        """Set rule in policy to enable/disable
        
        Endpoint: `PUT /management-rest/comm-control/set-policy-rule-state`
        
        Args:
            organization: Target organization in an MSSP environment (optional).
            policyName: (Required) Specifies policy name
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
            "/management-rest/comm-control/set-policy-rule-state",
            params={
            "policyName": policyName,
            "ruleName": ruleName,
            "state": state
        },
            organization=organization,
        )

