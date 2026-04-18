"""Curated threat hunting tools.

Versions with docstrings full of smarter examples that understand the
FortiEDR threat-hunting query language.
"""
from __future__ import annotations

import logging
from typing import Any

from mcp.server.fastmcp import FastMCP

from ...auth import AuthManager
from ...client import FortiEDRClient
from .events import _normalize_date, _window_to_bounds

log = logging.getLogger(__name__)

OVERRIDES = {
    "threat_hunting_search",
    "threat_hunting_facets",
    "threat_hunting_counts",
}

# Presets accepted by FortiEDR's `time` field on threat-hunting endpoints
_TH_PRESETS = {
    "lastHour", "last12hours", "last24hours", "last7days",
    "last30days", "lastYear",
}


def _build_time_body(
    time: str | None,
    time_window: str | None,
    time_from: str | None,
    time_to: str | None,
) -> dict[str, Any]:
    """Produce the portion of a threat-hunting body that describes the time range.

    FortiEDR is strict:
    - `time` must be one of the presets (lastHour, last24hours, last7days...)
      OR the literal 'custom' when `fromTime`/`toTime` are supplied.
    - `fromTime`/`toTime` must be 'yyyy-MM-dd HH:mm:ss' (not ISO 8601).
    """
    out: dict[str, Any] = {}

    if time and time != "custom":
        if time not in _TH_PRESETS:
            raise ValueError(
                f"Invalid time preset {time!r}. "
                f"Use one of {sorted(_TH_PRESETS)} or 'custom'."
            )
        out["time"] = time
        return out

    if time_window and not (time_from or time_to):
        time_from, time_to = _window_to_bounds(time_window)

    if time_from or time_to:
        out["time"] = "custom"
        if time_from:
            out["fromTime"] = _normalize_date(time_from)
        if time_to:
            out["toTime"] = _normalize_date(time_to)
    return out


def register_read(mcp: FastMCP, auth: AuthManager) -> None:
    @mcp.tool(name="threat_hunting_search")
    async def threat_hunting_search(
        query: str,
        organization: str | None = None,
        devices: list[str] | None = None,
        time: str | None = None,
        time_window: str | None = None,
        time_from: str | None = None,
        time_to: str | None = None,
        limit: int = 1000,
        sort_field: str | None = None,
        sort_direction: str | None = None,
    ) -> Any:
        """Run a query in FortiEDR Threat Hunting.

        Query language examples:
        - Process events for PowerShell: `Category:Process AND Source.Process.Name:"powershell.exe"`
        - LOLBins: `Source.Process.Name:("rundll32.exe" OR "regsvr32.exe" OR "certutil.exe")`
        - Network activity from a process: `Category:Network AND Source.Process.Name:"curl.exe"`
        - Hash search: `Source.Process.File.SHA256:"<hash>"`

        IMPORTANT — valid `Category` values: File, Process, Network, Registry, Log.
        IMPORTANT — valid `Type` values include (not exhaustive):
            "Executable Loaded", "Socket Connect", "Socket Listen",
            "Key Saved", "Trace Entry Created", "Log Entry Created".
        DO NOT use "Process Creation" or "Network Connection" — these are
        FortiEDR Events terminology, not Threat Hunting. TH uses Category
        and Type enums above.

        CommandLine / Path wildcard search is limited — these fields are
        tokenised, so `*AppData*` will not match. Use exact substrings.

        Time handling — pick ONE of:
        - `time` preset: lastHour, last12hours, last24hours, last7days, last30days, lastYear
        - `time_window`: "24h", "7d", "30m" (converted to fromTime/toTime)
        - `time_from`/`time_to`: absolute bounds

        ISO 8601 is accepted and normalised to FortiEDR's required
        'yyyy-MM-dd HH:mm:ss' format automatically.

        Args:
            query: A FortiEDR query-language expression.
            organization: Target tenant (MSSP).
            devices: Search only within the listed devices.
            time: A preset value like 'last24hours' (preferred for relative windows).
            time_window: Shortcut like '24h', '7d' — triggers a custom window.
            time_from: Absolute start time.
            time_to: Absolute end time.
            limit: Maximum records to return (FortiEDR caps at 1000).
            sort_field: Sort field (e.g. 'Time').
            sort_direction: 'asc' or 'desc'.
        """
        if limit > 1000:
            limit = 1000
        body: dict[str, Any] = {"query": query, "itemsPerPage": limit}
        body.update(_build_time_body(time, time_window, time_from, time_to))
        if devices:
            body["devices"] = devices
        if sort_field:
            body["sortBy"] = sort_field
        if sort_direction:
            body["sortDirection"] = sort_direction

        log.info("threat_hunting_search body=%s", body)
        async with _client(auth) as c:
            return await c.post(
                "/management-rest/threat-hunting/search",
                json_body=body,
                organization=auth.resolve_org(organization),
            )

    @mcp.tool(name="threat_hunting_facets")
    async def threat_hunting_facets(
        facet_fields: list[str],
        query: str | None = None,
        organization: str | None = None,
        time: str | None = None,
        time_window: str | None = None,
        time_from: str | None = None,
        time_to: str | None = None,
        top_n: int = 10,
    ) -> Any:
        """Return the distribution of specific fields over events matching the query (facet).

        Valid `facet_fields` values (verified working):
        - `Source.Process.Name` — distribution of process names
        - `Target.Process.Name` — target/child process names
        - `Device.Name` — which endpoints generated the events
        - `Category` — values: File, Process, Network, Registry, Log
        - `Type` — values: "Socket Connect", "Executable Loaded",
            "Key Saved", "Trace Entry Created", "Log Entry Created", etc.
        - `Source.Process.File.SHA256` — hash distribution

        Fields that DO NOT work (FortiEDR returns "Transaction rolled back"):
        Source.Parent.Name, Source.User.Name, Source.Process.Path

        Example — top 10 process names running in the last hour:
            facet_fields=['Source.Process.Name'], time='lastHour'

        `query` is optional. Omit it to facet all events in the window.

        Time: same rules as threat_hunting_search — use `time` preset
        (last24hours etc.) or `time_window`/`time_from`+`time_to`.
        """
        facets = [
            {"fieldName": f, "numOfDisplayedItems": top_n, "order": i + 1}
            for i, f in enumerate(facet_fields)
        ]
        body: dict[str, Any] = {"facets": facets}
        if query:
            body["query"] = query
        body.update(_build_time_body(time, time_window, time_from, time_to))
        log.info("threat_hunting_facets body=%s", body)
        async with _client(auth) as c:
            return await c.post(
                "/management-rest/threat-hunting/facets",
                json_body=body,
                organization=auth.resolve_org(organization),
            )

    @mcp.tool(name="threat_hunting_counts")
    async def threat_hunting_counts(
        query: str,
        organization: str | None = None,
        time: str | None = None,
        time_window: str | None = None,
        time_from: str | None = None,
        time_to: str | None = None,
        group_by_device: bool = False,
    ) -> Any:
        """Return the number of events matching the query — optionally grouped by device.

        Ideal for quick IoC sweeps: "On how many distinct endpoints did this
        hash execute?"

        Time: same rules as threat_hunting_search — use `time` preset
        (last24hours etc.) or `time_window`/`time_from`+`time_to`.
        """
        body: dict[str, Any] = {"query": query}
        body.update(_build_time_body(time, time_window, time_from, time_to))
        if group_by_device:
            body["groupByDevice"] = True
        log.info("threat_hunting_counts body=%s", body)
        async with _client(auth) as c:
            return await c.post(
                "/management-rest/threat-hunting/counts",
                json_body=body,
                organization=auth.resolve_org(organization),
            )


def _client(auth: AuthManager) -> FortiEDRClient:
    cfg = auth.config
    return FortiEDRClient(
        host=cfg.host, user=cfg.user, password=cfg.password,
        default_org=cfg.default_org, verify_ssl=cfg.verify_ssl,
    )
