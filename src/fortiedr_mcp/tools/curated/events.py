"""Curated event tools — richer docstrings, smarter parameters, and
helpers for FP/TP triage.

Overrides the generated `events_list_events`, `events_count_events` and
`events_list_raw_data_items` tools.
"""
from __future__ import annotations

import logging
import re
from datetime import datetime, timedelta, timezone
from typing import Any

from mcp.server.fastmcp import FastMCP

from ...auth import AuthManager
from ...client import FortiEDRClient

log = logging.getLogger(__name__)

_WINDOW_RE = re.compile(r"^\s*(\d+)\s*([smhdw])\s*$", re.IGNORECASE)
_UNIT_SECONDS = {"s": 1, "m": 60, "h": 3600, "d": 86400, "w": 604800}

_FORTIEDR_FMT = "%Y-%m-%d %H:%M:%S"


def _window_to_bounds(window: str) -> tuple[str, str]:
    """Convert '24h', '7d', '30m' to (firstSeenFrom, firstSeenTo) in UTC."""
    m = _WINDOW_RE.match(window)
    if not m:
        raise ValueError(
            f"Invalid time_window '{window}'. Use '<N><unit>' with unit in s/m/h/d/w."
        )
    n, unit = int(m.group(1)), m.group(2).lower()
    now = datetime.now(timezone.utc)
    since = now - timedelta(seconds=n * _UNIT_SECONDS[unit])
    return since.strftime(_FORTIEDR_FMT), now.strftime(_FORTIEDR_FMT)


def _normalize_date(value: str | None) -> str | None:
    """Accept ISO 8601 ('2026-04-17T02:59:42Z', '...+00:00') and a few common
    variants, return the FortiEDR-expected 'YYYY-MM-DD HH:mm:ss' in UTC.

    Returns the input untouched if it already matches FortiEDR format or if
    parsing fails (so the caller still sees an error from the server).
    """
    if not value:
        return value
    s = value.strip()
    # Already FortiEDR-style
    if re.match(r"^\d{4}-\d{2}-\d{2}( \d{2}:\d{2}:\d{2})?$", s):
        return s
    try:
        # datetime.fromisoformat handles '2026-04-17T02:59:42+00:00'
        # but not trailing 'Z' before 3.11 — normalize it
        iso = s.replace("Z", "+00:00")
        dt = datetime.fromisoformat(iso)
        if dt.tzinfo is not None:
            dt = dt.astimezone(timezone.utc).replace(tzinfo=None)
        return dt.strftime(_FORTIEDR_FMT)
    except ValueError:
        return value

# Names of generated tools overridden here
OVERRIDES = {
    "events_list_events",
    "events_count_events",
    "events_list_raw_data_items",
}

# Fixed values accepted by FortiEDR — exposed as hints for the analyst
SEVERITIES = ["Critical", "High", "Medium", "Low"]
CLASSIFICATIONS = [
    "Malicious", "Suspicious", "Inconclusive", "Likely Safe", "PUP", "Safe"
]
EVENT_ACTIONS = ["Block", "Log", "Simulation Block"]


def register_read(mcp: FastMCP, auth: AuthManager) -> None:
    @mcp.tool(name="events_list_events")
    async def events_list_events(
        organization: str | None = None,
        severity: list[str] | None = None,
        classification: list[str] | None = None,
        handled: bool | None = None,
        archived: bool | None = None,
        seen: bool | None = None,
        time_window: str | None = None,
        first_seen_from: str | None = None,
        first_seen_to: str | None = None,
        last_seen_from: str | None = None,
        last_seen_to: str | None = None,
        device: str | None = None,
        process: str | None = None,
        destinations: str | None = None,
        rule_name: str | None = None,
        raw_data_id: int | None = None,
        limit: int | None = 100,
    ) -> Any:
        """List FortiEDR security events with filters.

        The most heavily used tool in this MCP. Suitable for triage,
        hunting, and reporting.

        Common prompt → parameter mapping:
        - "open/unhandled events" → handled=False
        - "archived events" → archived=True
        - "unread events" → seen=False
        - "critical events" → severity=["Critical"]
        - "malicious events" → classification=["Malicious"]
        - "last 24 hours" → time_window="24h"
        - "last 7 days" → time_window="7d"
        - "last 30 minutes" → time_window="30m"

        time_window shortcut: set this instead of first_seen_from/to for
        relative windows. Supported units: s/m/h/d/w. Example: "24h", "7d".
        If you also pass first_seen_from/to, those win.

        Valid values:
        - severity: Critical, High, Medium, Low
        - classification: Malicious, Suspicious, Inconclusive, Likely Safe, PUP, Safe

        Absolute date format: 'YYYY-MM-DD HH:mm:ss' or 'YYYY-MM-DD'.

        MSSP tip: if `organization` is omitted, the default org is used.
        To scan every tenant, first call `organizations_list_organizations`
        and then invoke this tool for each org.

        Args:
            organization: Target tenant (MSSP). Defaults to the default org.
            severity: Severity list (OR-combined).
            classification: Classification list.
            handled: true=handled, false=open, none=all.
            archived: true=archived, false=not archived, none=all.
            seen: true=seen/read, false=unread, none=all.
            time_window: Relative window like "24h", "7d", "30m". Computed
                against now in UTC and passed as firstSeenFrom/firstSeenTo.
            first_seen_from: Absolute lower bound for first seen (UTC).
            first_seen_to: Absolute upper bound for first seen (UTC).
            last_seen_from: Lower bound for last seen.
            last_seen_to: Upper bound for last seen.
            device: Device name filter (partial match).
            process: Process name filter.
            destinations: Destination (IP/domain) filter.
            rule_name: Triggered rule name.
            raw_data_id: A specific raw data event ID.
            limit: Maximum number of events to return. Default 100.
        """
        if time_window and not (first_seen_from or first_seen_to):
            first_seen_from, first_seen_to = _window_to_bounds(time_window)
        if limit is not None and limit > 1000:
            limit = 1000  # FortiEDR caps itemsPerPage at 1000

        params = {
            # NOTE: FortiEDR uses PLURAL 'severities' / 'classifications'
            "severities": ",".join(severity) if severity else None,
            "classifications": ",".join(classification) if classification else None,
            "handled": handled,
            "archived": archived,
            "seen": seen,
            "firstSeenFrom": _normalize_date(first_seen_from),
            "firstSeenTo": _normalize_date(first_seen_to),
            "lastSeenFrom": _normalize_date(last_seen_from),
            "lastSeenTo": _normalize_date(last_seen_to),
            "device": device,
            "process": process,
            "destinations": destinations,
            "rule": rule_name,
            "rawDataId": raw_data_id,
            "itemsPerPage": limit,
        }
        resolved_org = auth.resolve_org(organization)
        log.info(
            "events_list_events called | org=%s | params=%s",
            resolved_org, {k: v for k, v in params.items() if v is not None},
        )
        async with _client(auth) as c:
            resp = await c.get(
                "/management-rest/events/list-events",
                params=params,
                organization=resolved_org,
            )
        count = len(resp) if isinstance(resp, list) else (
            len(resp.get("data", [])) if isinstance(resp, dict) else 0
        )
        log.info("events_list_events returned %d items", count)
        return resp

    @mcp.tool(name="events_count_events")
    async def events_count_events(
        organization: str | None = None,
        severity: list[str] | None = None,
        classification: list[str] | None = None,
        handled: bool | None = None,
        archived: bool | None = None,
        time_window: str | None = None,
        first_seen_from: str | None = None,
        first_seen_to: str | None = None,
        device: str | None = None,
        process: str | None = None,
        destinations: str | None = None,
        rule_name: str | None = None,
    ) -> Any:
        """Return the number of events matching the filter.

        Ideal for dashboards, reporting, and trend analysis — use this
        when you only need the count and not the full list.

        time_window shortcut: "24h", "7d", "30m" etc. See
        events_list_events for the full mapping.
        """
        if time_window and not (first_seen_from or first_seen_to):
            first_seen_from, first_seen_to = _window_to_bounds(time_window)
        params = {
            "severities": ",".join(severity) if severity else None,
            "classifications": ",".join(classification) if classification else None,
            "handled": handled,
            "archived": archived,
            "firstSeenFrom": _normalize_date(first_seen_from),
            "firstSeenTo": _normalize_date(first_seen_to),
            "device": device,
            "process": process,
            "destinations": destinations,
            "rule": rule_name,
        }
        async with _client(auth) as c:
            return await c.get(
                "/management-rest/events/count-events",
                params=params,
                organization=auth.resolve_org(organization),
            )

    @mcp.tool(name="events_list_raw_data_items")
    async def events_list_raw_data_items(
        event_id: int,
        organization: str | None = None,
    ) -> Any:
        """Fetch the raw data records for an event — process chain,
        command line, hash, signer, network destinations.

        The MOST IMPORTANT tool for FP/TP triage. Always drill into the
        event with this before deciding.

        Args:
            event_id: Event ID (the id field returned by list_events).
            organization: Target tenant (MSSP).
        """
        async with _client(auth) as c:
            return await c.get(
                "/management-rest/events/list-raw-data-items",
                params={"eventId": event_id},
                organization=auth.resolve_org(organization),
            )


def register_write(mcp: FastMCP, auth: AuthManager) -> None:
    @mcp.tool(name="events_update")
    async def events_update(
        event_ids: list[int],
        organization: str | None = None,
        classification: str | None = None,
        handled: bool | None = None,
        comment: str | None = None,
    ) -> Any:
        """Classify / close / comment on one or more events.

        In an MDR workflow this should only run after analyst approval.
        You are strongly encouraged to put audit metadata into the
        comment field when invoking this tool:

            "AI-assisted triage | analyst: <name> | ticket: <number>"

        Args:
            event_ids: IDs of events to update.
            organization: Target tenant (MSSP).
            classification: New classification: Malicious, Suspicious,
                Inconclusive, Likely Safe, PUP, Safe.
            handled: True to close the event, False to reopen it.
            comment: Comment to append (keep required for audit).
        """
        body: dict[str, Any] = {"eventIds": event_ids}
        if classification:
            body["classification"] = classification
        if handled is not None:
            body["handled"] = handled
        if comment:
            body["comment"] = comment
        async with _client(auth) as c:
            return await c.put(
                "/management-rest/events",
                json_body=body,
                organization=auth.resolve_org(organization),
            )


# --- helper -----------------------------------------------------------
def _client(auth: AuthManager) -> FortiEDRClient:
    cfg = auth.config
    return FortiEDRClient(
        host=cfg.host,
        user=cfg.user,
        password=cfg.password,
        default_org=cfg.default_org,
        verify_ssl=cfg.verify_ssl,
    )
