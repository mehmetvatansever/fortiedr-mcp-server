"""MDR reporting composite tools.

Data-collection tools for monthly/weekly customer reports. Output is
structured JSON — Claude/Copilot can then format it as docx/xlsx/md.
"""
from __future__ import annotations

import asyncio
from typing import Any

from mcp.server.fastmcp import FastMCP

from ...auth import AuthManager
from ...client import FortiEDRClient


def register_read(mcp: FastMCP, auth: AuthManager) -> None:
    @mcp.tool(name="mdr_monthly_report_data")
    async def mdr_monthly_report_data(
        first_seen_from: str,
        first_seen_to: str,
        organization: str | None = None,
    ) -> dict[str, Any]:
        """Gather all data needed for a monthly/weekly customer report in a single call.

        Returned fields:
        - event_counts: counts by severity and classification
        - top_affected_devices: the 10 endpoints with the most events
        - top_rules: the 10 most-triggered security rules
        - collector_inventory: collector counts by state
        - dashboard: FortiEDR dashboard summary
        - audit_summary: admin operations performed during the window

        Claude can then turn this data into a polished report using the
        docx skill.

        Args:
            first_seen_from: Window start as 'YYYY-MM-DD' or ISO 8601.
            first_seen_to: Window end.
            organization: Target tenant. Defaults to the default org.
        """
        org = auth.resolve_org(organization)

        async def _count_by_severity():
            async with _client(auth) as c:
                results = {}
                for sev in ["Critical", "High", "Medium", "Low"]:
                    try:
                        resp = await c.get(
                            "/management-rest/events/count-events",
                            params={
                                "severities": sev,
                                "firstSeenFrom": first_seen_from,
                                "firstSeenTo": first_seen_to,
                            },
                            organization=org,
                        )
                        results[sev] = _extract_count(resp)
                    except Exception as e:
                        results[sev] = {"error": str(e)}
                return results

        async def _count_by_classification():
            async with _client(auth) as c:
                results = {}
                for cls in ["Malicious", "Suspicious", "Inconclusive",
                            "Likely Safe", "PUP", "Safe"]:
                    try:
                        resp = await c.get(
                            "/management-rest/events/count-events",
                            params={
                                "classifications": cls,
                                "firstSeenFrom": first_seen_from,
                                "firstSeenTo": first_seen_to,
                            },
                            organization=org,
                        )
                        results[cls] = _extract_count(resp)
                    except Exception as e:
                        results[cls] = {"error": str(e)}
                return results

        async def _events_for_analysis():
            """Fetch the full event list for top devices/rules analysis."""
            async with _client(auth) as c:
                try:
                    resp = await c.get(
                        "/management-rest/events/list-events",
                        params={
                            "firstSeenFrom": first_seen_from,
                            "firstSeenTo": first_seen_to,
                        },
                        organization=org,
                    )
                    return resp
                except Exception as e:
                    return {"error": str(e)}

        async def _collectors():
            async with _client(auth) as c:
                try:
                    return await c.get(
                        "/management-rest/inventory/list-collectors",
                        organization=org,
                    )
                except Exception as e:
                    return {"error": str(e)}

        async def _dashboard():
            async with _client(auth) as c:
                try:
                    most_targeted = await c.get(
                        "/api/dashboard/most-targeted-items",
                        organization=org,
                    )
                    unhandled = await c.get(
                        "/api/dashboard/unhandled-items",
                        organization=org,
                    )
                    return {"most_targeted": most_targeted, "unhandled": unhandled}
                except Exception as e:
                    return {"error": str(e)}

        async def _audit():
            async with _client(auth) as c:
                try:
                    return await c.get(
                        "/management-rest/audit/get-audit",
                        params={"fromDate": first_seen_from, "toDate": first_seen_to},
                        organization=org,
                    )
                except Exception as e:
                    return {"error": str(e)}

        # Run them all in parallel
        sev_counts, cls_counts, events, collectors, dashboard, audit = await asyncio.gather(
            _count_by_severity(),
            _count_by_classification(),
            _events_for_analysis(),
            _collectors(),
            _dashboard(),
            _audit(),
            return_exceptions=True,
        )

        # Derive top devices / rules from the event list
        top_devices = _top_n_by_field(events, field_candidates=["device", "deviceName", "collector"])
        top_rules = _top_n_by_field(events, field_candidates=["rule", "ruleName", "ruleNames"])
        collector_states = _group_collectors_by_state(collectors)

        return {
            "organization": org,
            "window": {"from": first_seen_from, "to": first_seen_to},
            "event_counts": {
                "by_severity": _or_error(sev_counts),
                "by_classification": _or_error(cls_counts),
                "total": sum(
                    v for v in (_or_error(sev_counts) or {}).values()
                    if isinstance(v, int)
                ) if not isinstance(sev_counts, Exception) else None,
            },
            "top_affected_devices": top_devices,
            "top_rules": top_rules,
            "collector_inventory": collector_states,
            "dashboard": _or_error(dashboard),
            "audit_summary": _summarize_audit(audit),
        }


# --- helpers ------------------------------------------------------------
def _extract_count(resp: Any) -> int | dict:
    if isinstance(resp, int):
        return resp
    if isinstance(resp, dict):
        for key in ("count", "total", "data"):
            v = resp.get(key)
            if isinstance(v, int):
                return v
            if isinstance(v, list):
                return len(v)
    if isinstance(resp, list):
        return len(resp)
    return {"unknown_response_shape": str(type(resp).__name__)}


def _top_n_by_field(events: Any, field_candidates: list[str], n: int = 10) -> list[dict]:
    if isinstance(events, (Exception, dict)) and (not isinstance(events, dict) or "error" in events):
        return []
    items = events if isinstance(events, list) else events.get("data") if isinstance(events, dict) else None
    if not isinstance(items, list):
        return []
    counts: dict[str, int] = {}
    for it in items:
        if not isinstance(it, dict):
            continue
        val = None
        for f in field_candidates:
            val = it.get(f)
            if val:
                break
        if isinstance(val, list):
            for sub in val:
                key = str(sub)
                counts[key] = counts.get(key, 0) + 1
        elif val:
            key = str(val)
            counts[key] = counts.get(key, 0) + 1
    top = sorted(counts.items(), key=lambda x: x[1], reverse=True)[:n]
    return [{"value": k, "count": v} for k, v in top]


def _group_collectors_by_state(collectors: Any) -> dict[str, int]:
    if isinstance(collectors, (Exception,)) or (isinstance(collectors, dict) and "error" in collectors):
        return {}
    items = collectors if isinstance(collectors, list) else collectors.get("data") if isinstance(collectors, dict) else None
    if not isinstance(items, list):
        return {}
    out: dict[str, int] = {}
    for c in items:
        if not isinstance(c, dict):
            continue
        state = c.get("state") or c.get("status") or "Unknown"
        out[str(state)] = out.get(str(state), 0) + 1
    out["total"] = sum(v for k, v in out.items() if k != "total")
    return out


def _summarize_audit(audit: Any) -> dict[str, Any]:
    if isinstance(audit, (Exception,)) or (isinstance(audit, dict) and "error" in audit):
        return {"error": str(audit) if isinstance(audit, Exception) else audit.get("error")}
    items = audit if isinstance(audit, list) else audit.get("data") if isinstance(audit, dict) else None
    if not isinstance(items, list):
        return {}
    action_counts: dict[str, int] = {}
    user_counts: dict[str, int] = {}
    for it in items:
        if not isinstance(it, dict):
            continue
        action = it.get("action") or it.get("operation") or "Unknown"
        user = it.get("user") or it.get("performedBy") or "Unknown"
        action_counts[str(action)] = action_counts.get(str(action), 0) + 1
        user_counts[str(user)] = user_counts.get(str(user), 0) + 1
    return {
        "total_actions": len(items),
        "top_actions": sorted(action_counts.items(), key=lambda x: x[1], reverse=True)[:10],
        "top_users": sorted(user_counts.items(), key=lambda x: x[1], reverse=True)[:10],
    }


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
