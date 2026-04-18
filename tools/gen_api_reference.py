"""Generate FortiEDR API reference documentation from the Postman collection.

Usage:
    python tools/gen_api_reference.py \
        fortiedr_api.postman_collection.json \
        docs/api-reference.md
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


def _url_to_path(url: Any) -> tuple[str, list[str]]:
    """Return (path, query_param_names) from a Postman URL object."""
    if isinstance(url, str):
        return url, []
    if not isinstance(url, dict):
        return "", []
    raw = url.get("raw", "")
    # {{baseUrl}}/foo/bar -> /foo/bar
    path = raw
    if "{{" in raw and "}}" in raw:
        # Take the part after the first }}
        path = raw.split("}}", 1)[1] if "}}" in raw else raw
    elif path.startswith(("http://", "https://")):
        # Bare URL — strip scheme + host, keep path only
        no_scheme = path.split("://", 1)[1]
        slash = no_scheme.find("/")
        path = no_scheme[slash:] if slash >= 0 else "/"
    # Strip the query string
    if "?" in path:
        path = path.split("?", 1)[0]
    query_names = [q.get("key", "") for q in url.get("query", []) if isinstance(q, dict)]
    return path, query_names


def _body_summary(body: Any) -> str | None:
    if not isinstance(body, dict):
        return None
    mode = body.get("mode")
    if mode == "raw":
        raw = body.get("raw", "")
        if not raw.strip():
            return None
        # JSON?
        try:
            parsed = json.loads(raw)
            if isinstance(parsed, dict):
                keys = list(parsed.keys())
                return f"JSON body, fields: `{', '.join(keys[:15])}`" + ("..." if len(keys) > 15 else "")
            if isinstance(parsed, list):
                return f"JSON array ({len(parsed)} sample records)"
        except json.JSONDecodeError:
            pass
        return f"Raw body ({len(raw)} chars)"
    if mode == "formdata":
        fields = [f.get("key", "") for f in body.get("formdata", [])]
        return f"form-data: {', '.join(fields[:10])}"
    if mode == "urlencoded":
        fields = [f.get("key", "") for f in body.get("urlencoded", [])]
        return f"urlencoded: {', '.join(fields[:10])}"
    if mode == "file":
        return "Binary file upload"
    return None


def _description(desc: Any) -> str:
    if isinstance(desc, str):
        return desc.strip()
    if isinstance(desc, dict):
        return (desc.get("content") or "").strip()
    return ""


def collect_endpoints(items: list[dict], category: str = "", depth: int = 0) -> list[dict]:
    """Flatten every endpoint into a single list.

    Uses the first two tree levels as category (e.g. 'management-rest / events').
    Deeper levels are folded into the endpoint name.
    """
    out: list[dict] = []
    for it in items:
        name = it.get("name", "")
        if "request" in it:
            req = it["request"]
            if not isinstance(req, dict):
                continue
            path, query = _url_to_path(req.get("url"))
            out.append({
                "category": category or "uncategorized",
                "name": name,
                "method": req.get("method", "GET"),
                "path": path,
                "query": query,
                "body": _body_summary(req.get("body")),
                "description": _description(req.get("description")),
            })
        else:
            # Use the first two levels as category
            if depth < 2:
                new_cat = f"{category} / {name}" if category else name
            else:
                new_cat = category
            out.extend(collect_endpoints(it.get("item", []), new_cat, depth + 1))
    return out


def render_markdown(endpoints: list[dict]) -> str:
    lines: list[str] = []
    lines.append("# FortiEDR API Reference")
    lines.append("")
    lines.append("This file is auto-generated from the official Postman collection.")
    lines.append("Regenerate with the `tools/gen_api_reference.py` script.")
    lines.append("")
    lines.append(f"**Total endpoints:** {len(endpoints)}")
    lines.append("")

    # Group by category
    by_category: dict[str, list[dict]] = {}
    for ep in endpoints:
        by_category.setdefault(ep["category"], []).append(ep)

    # Table of contents
    lines.append("## Table of Contents")
    lines.append("")
    for cat in sorted(by_category):
        anchor = cat.lower().replace(" ", "-").replace("/", "").replace("--", "-")
        lines.append(f"- [{cat}](#{anchor}) ({len(by_category[cat])})")
    lines.append("")
    lines.append("---")
    lines.append("")

    for cat in sorted(by_category):
        lines.append(f"## {cat}")
        lines.append("")
        # Single-table method/path summary
        lines.append("| Method | Path | Name |")
        lines.append("|---|---|---|")
        for ep in by_category[cat]:
            path = ep["path"] or "-"
            lines.append(f"| `{ep['method']}` | `{path}` | {ep['name']} |")
        lines.append("")

        # Details
        for ep in by_category[cat]:
            lines.append(f"### `{ep['method']}` {ep['name']}")
            lines.append("")
            if ep["path"]:
                lines.append(f"**Path:** `{ep['path']}`")
                lines.append("")
            if ep["query"]:
                lines.append(f"**Query params:** {', '.join(f'`{q}`' for q in ep['query'])}")
                lines.append("")
            if ep["body"]:
                lines.append(f"**Body:** {ep['body']}")
                lines.append("")
            if ep["description"]:
                lines.append("**Description:**")
                lines.append("")
                lines.append("> " + ep["description"].replace("\n", "\n> "))
                lines.append("")
            lines.append("---")
            lines.append("")

    return "\n".join(lines)


def main() -> None:
    if len(sys.argv) != 3:
        print("Usage: gen_api_reference.py <postman.json> <output.md>", file=sys.stderr)
        sys.exit(1)

    src = Path(sys.argv[1])
    dst = Path(sys.argv[2])

    data = json.loads(src.read_text())
    endpoints = collect_endpoints(data.get("item", []))
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(render_markdown(endpoints))
    print(f"Done: {len(endpoints)} endpoints written to {dst}")


if __name__ == "__main__":
    main()
