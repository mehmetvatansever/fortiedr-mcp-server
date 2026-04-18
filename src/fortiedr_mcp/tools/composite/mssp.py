"""MSSP / cross-tenant composite tools.

The tools in this module do not map to a single FortiEDR endpoint —
they combine several endpoints to deliver business value for MDR
operations.
"""
from __future__ import annotations

import asyncio
import logging
from typing import Any

from mcp.server.fastmcp import FastMCP

from ...auth import AuthManager
from ...client import FortiEDRClient
from ..curated.events import _normalize_date, _window_to_bounds

log = logging.getLogger(__name__)


def register_read(mcp: FastMCP, auth: AuthManager) -> None:
    @mcp.tool(name="mssp_events_aggregate")
    async def mssp_events_aggregate(
        archived: bool | None = None,
        handled: bool | None = None,
        seen: bool | None = None,
        severity: list[str] | None = None,
        classification: list[str] | None = None,
        time_window: str | None = None,
        first_seen_from: str | None = None,
        first_seen_to: str | None = None,
        device: str | None = None,
        process: str | None = None,
        limit: int | None = 500,
    ) -> Any:
        """List events across the WHOLE MSSP console in one call.

        Use this instead of `events_list_events` whenever the user asks
        for "all customers", "everyone", "MSSP-wide", or when a single-org
        call returns 0 results unexpectedly. This tool explicitly DOES
        NOT send an `organization` query parameter, so FortiEDR returns
        aggregated data across every tenant visible to the API user.

        Common mappings:
        - "all archived events in the last 24h" → archived=True, time_window="24h"
        - "all open events today" → handled=False, time_window="24h"

        time_window: shortcut like "24h", "7d", "30m".

        Args:
            archived: true=archived only, false=non-archived, none=all.
            handled: true=handled, false=open, none=all.
            seen: true=seen/read, false=unread.
            severity: Critical, High, Medium, Low (OR-combined).
            classification: Malicious, Suspicious, Inconclusive, Likely Safe, PUP, Safe.
            time_window: Relative window string ("24h", "7d"...).
            first_seen_from: Absolute start time (UTC).
            first_seen_to: Absolute end time (UTC).
            device: Device name filter.
            process: Process name filter.
            limit: Maximum events to return. Default 500.
        """
        if time_window and not (first_seen_from or first_seen_to):
            first_seen_from, first_seen_to = _window_to_bounds(time_window)
        if limit is not None and limit > 1000:
            limit = 1000  # FortiEDR caps itemsPerPage at 1000

        params = {
            "archived": archived,
            "handled": handled,
            "seen": seen,
            "severities": ",".join(severity) if severity else None,
            "classifications": ",".join(classification) if classification else None,
            "firstSeenFrom": _normalize_date(first_seen_from),
            "firstSeenTo": _normalize_date(first_seen_to),
            "device": device,
            "process": process,
            "itemsPerPage": limit,
        }
        log.info(
            "mssp_events_aggregate called (no org filter) | params=%s",
            {k: v for k, v in params.items() if v is not None},
        )
        # Build a client with default_org=None so the default from config
        # is NOT silently injected as ?organization=...
        cfg = auth.config
        async with FortiEDRClient(
            host=cfg.host, user=cfg.user, password=cfg.password,
            default_org=None, verify_ssl=cfg.verify_ssl,
        ) as c:
            resp = await c.get(
                "/management-rest/events/list-events",
                params=params,
                organization=None,
            )
        count = len(resp) if isinstance(resp, list) else (
            len(resp.get("data", [])) if isinstance(resp, dict) else 0
        )
        log.info("mssp_events_aggregate returned %d items", count)
        return resp

    @mcp.tool(name="mssp_event_summary_by_org")
    async def mssp_event_summary_by_org(
        first_seen_from: str | None = None,
        first_seen_to: str | None = None,
        severity: list[str] | None = None,
        handled: bool | None = False,
    ) -> dict[str, Any]:
        """Summarise event counts across every tenant, grouped by organization.

        The most valuable tool for MDR morning triage. Fetches the event
        count for each org in parallel and sorts the busiest tenants first.

        Sample prompt: "Summarise the last 8 hours of handled=false Critical
        and High events by customer."

        Args:
            first_seen_from: Start time.
            first_seen_to: End time.
            severity: Severity filter.
            handled: Closed/open filter. Default: False (open events only).
        """
        async with _client(auth) as c:
            orgs_resp = await c.get("/management-rest/organizations/list-organizations")

        org_names = _extract_org_names(orgs_resp)
        if not org_names:
            return {"error": "Could not retrieve the organization list", "raw": orgs_resp}

        params_base = {
            "severities": ",".join(severity) if severity else None,
            "handled": handled,
            "firstSeenFrom": first_seen_from,
            "firstSeenTo": first_seen_to,
        }

        async def _count_for_org(org: str) -> tuple[str, int | str]:
            try:
                async with _client(auth) as c:
                    resp = await c.get(
                        "/management-rest/events/count-events",
                        params=params_base,
                        organization=org,
                    )
                # FortiEDR response shape: {"count": N} or a raw int
                if isinstance(resp, dict):
                    count = resp.get("count") or resp.get("data") or 0
                    if isinstance(count, list):
                        count = len(count)
                elif isinstance(resp, int):
                    count = resp
                else:
                    count = 0
                return org, count
            except Exception as e:
                return org, f"error: {e}"

        results = await asyncio.gather(*[_count_for_org(o) for o in org_names])
        sorted_results = sorted(
            results,
            key=lambda x: (x[1] if isinstance(x[1], int) else -1),
            reverse=True,
        )
        return {
            "query_window": {"from": first_seen_from, "to": first_seen_to},
            "filters": {"severity": severity, "handled": handled},
            "total_orgs": len(org_names),
            "by_org": [{"organization": o, "event_count": c} for o, c in sorted_results],
        }

    @mcp.tool(name="mssp_ioc_sweep")
    async def mssp_ioc_sweep(
        ioc_value: str,
        ioc_type: str = "hash",
        time_from: str | None = None,
        time_to: str | None = None,
    ) -> dict[str, Any]:
        """Sweep for an IoC (hash, IP, domain, process) across every tenant.

        Used when fresh threat intelligence arrives. Runs a threat-hunting
        query per tenant and reports the number of affected customers and
        devices.

        Args:
            ioc_value: The value to search for (hash, IP, domain, process name).
            ioc_type: 'hash', 'ip', 'domain', 'process'. Default: hash.
            time_from: ISO 8601 start time.
            time_to: ISO 8601 end time.
        """
        # Build a query from the IoC type
        if ioc_type == "hash":
            length = len(ioc_value)
            field = {
                32: "MD5", 40: "SHA1", 64: "SHA256",
            }.get(length, "SHA256")
            query = f'Source.Process.File.{field}:"{ioc_value}"'
        elif ioc_type == "ip":
            query = f'Target.Network.RemoteIP:"{ioc_value}"'
        elif ioc_type == "domain":
            query = f'Target.Network.RemoteDomain:"{ioc_value}"'
        elif ioc_type == "process":
            query = f'Source.Process.Name:"{ioc_value}"'
        else:
            return {"error": f"Unknown ioc_type: {ioc_type}"}

        async with _client(auth) as c:
            orgs_resp = await c.get("/management-rest/organizations/list-organizations")
        org_names = _extract_org_names(orgs_resp)

        body: dict[str, Any] = {"query": query}
        if time_from: body["fromTime"] = time_from
        if time_to: body["toTime"] = time_to

        async def _hunt(org: str) -> tuple[str, Any]:
            try:
                async with _client(auth) as c:
                    resp = await c.post(
                        "/management-rest/threat-hunting/counts",
                        json_body=body,
                        organization=org,
                    )
                return org, resp
            except Exception as e:
                return org, {"error": str(e)}

        results = await asyncio.gather(*[_hunt(o) for o in org_names])
        affected = []
        clean = []
        errors = []
        for org, resp in results:
            if isinstance(resp, dict) and "error" in resp:
                errors.append({"organization": org, "error": resp["error"]})
                continue
            count = 0
            if isinstance(resp, dict):
                count = resp.get("count") or resp.get("total") or 0
            elif isinstance(resp, int):
                count = resp
            if count > 0:
                affected.append({"organization": org, "hit_count": count})
            else:
                clean.append(org)

        return {
            "ioc": {"type": ioc_type, "value": ioc_value, "query": query},
            "window": {"from": time_from, "to": time_to},
            "summary": {
                "total_orgs": len(org_names),
                "affected": len(affected),
                "clean": len(clean),
                "errors": len(errors),
            },
            "affected_orgs": sorted(affected, key=lambda x: x["hit_count"], reverse=True),
            "clean_orgs": clean,
            "errors": errors,
        }

    @mcp.tool(name="mdr_event_triage_brief")
    async def mdr_event_triage_brief(
        event_id: int,
        organization: str | None = None,
    ) -> dict[str, Any]:
        """Build an FP/TP triage brief for an event.

        A single call gathers:
        - Basic event metadata (list_events query by event_id)
        - Raw data (process chain, command line, hashes, signers)
        - Related exceptions (is there already a whitelist for similar patterns?)

        An analyst or an LLM can read this brief to make an informed FP/TP
        decision. This tool DOES NOT make a decision on its own — it only
        assembles context for analysis.

        Args:
            event_id: The FortiEDR event ID.
            organization: Target tenant.
        """
        org = auth.resolve_org(organization)

        async def _fetch_event():
            async with _client(auth) as c:
                return await c.get(
                    "/management-rest/events/list-events",
                    params={"rawDataId": event_id},
                    organization=org,
                )

        async def _fetch_raw():
            async with _client(auth) as c:
                return await c.get(
                    "/management-rest/events/list-raw-data-items",
                    params={"eventId": event_id},
                    organization=org,
                )

        async def _fetch_exceptions():
            async with _client(auth) as c:
                return await c.get(
                    "/management-rest/exceptions/get-event-exceptions",
                    params={"eventId": event_id},
                    organization=org,
                )

        event, raw, exceptions = await asyncio.gather(
            _fetch_event(), _fetch_raw(), _fetch_exceptions(),
            return_exceptions=True,
        )

        return {
            "event_id": event_id,
            "organization": org,
            "event": _or_error(event),
            "raw_data": _or_error(raw),
            "existing_exceptions": _or_error(exceptions),
            "hints": [
                "If the binary is signed and the publisher is trusted, FP is more likely.",
                "Suspicion rises when the parent process is 'outlook.exe' / 'winword.exe'.",
                "TP is more likely when the CommandLine contains -enc, -nop, or -w hidden.",
                "If there is already an exception for the same hash, a user has investigated it before.",
            ],
        }


def _extract_org_names(orgs_resp: Any) -> list[str]:
    """Extract org names from the FortiEDR list-organizations response."""
    if not isinstance(orgs_resp, (list, dict)):
        return []
    items = orgs_resp if isinstance(orgs_resp, list) else orgs_resp.get("data") or []
    names = []
    for item in items:
        if isinstance(item, dict):
            name = item.get("name") or item.get("accountName") or item.get("organization")
            if name:
                names.append(name)
        elif isinstance(item, str):
            names.append(item)
    return names


def _or_error(val: Any) -> Any:
    if isinstance(val, Exception):
        return {"error": str(val), "type": type(val).__name__}
    return val


def _client(auth: AuthManager) -> FortiEDRClient:
    cfg = auth.config
    return FortiEDRClient(
        host=cfg.host, user=cfg.user, password=cfg.password,
        default_org=cfg.default_org, verify_ssl=cfg.verify_ssl,
    )
