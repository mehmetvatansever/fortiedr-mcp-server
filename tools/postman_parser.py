"""Extract endpoint metadata from the Postman collection.

This module is used by both gen_api_reference.py and gen_tools.py.
"""
from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


@dataclass
class Endpoint:
    name: str
    method: str
    path: str
    category: str
    subcategory: str
    query_params: list[dict[str, Any]] = field(default_factory=list)
    path_params: list[str] = field(default_factory=list)
    body_schema: dict[str, Any] | None = None
    body_type: str | None = None  # "json", "formdata", "urlencoded", "file", None
    description: str = ""

    @property
    def full_category(self) -> str:
        return f"{self.category}/{self.subcategory}" if self.subcategory else self.category

    @property
    def slug(self) -> str:
        """A snake_case slug suitable as a tool name."""
        base = self.name.strip().lower()
        # Turn whitespace into _
        base = re.sub(r"[\s\-]+", "_", base)
        # Drop non-alphanumeric leading characters
        base = re.sub(r"[^a-z0-9_]", "", base)
        base = re.sub(r"_+", "_", base).strip("_")
        return base or "unnamed"

    @property
    def python_fn_name(self) -> str:
        """Python function name — snake_case with a category prefix."""
        cat = self.subcategory.replace("-", "_") if self.subcategory else self.category.replace("-", "_")
        slug = self.slug
        # Avoid repeating the category if it is already the slug prefix
        if slug.startswith(cat):
            return slug
        return f"{cat}_{slug}"


def _description(desc: Any) -> str:
    if isinstance(desc, str):
        return desc.strip()
    if isinstance(desc, dict):
        return (desc.get("content") or "").strip()
    return ""


def _parse_url(url: Any) -> tuple[str, list[dict[str, Any]], list[str]]:
    """Return the Postman URL as (path, query_params, path_params)."""
    if isinstance(url, str):
        return url, [], []
    if not isinstance(url, dict):
        return "", [], []

    raw = url.get("raw", "")
    path = raw
    if "}}" in raw:
        path = raw.split("}}", 1)[1]
    elif path.startswith(("http://", "https://")):
        # Bare URL without {{baseUrl}} — strip scheme + host, keep path only
        no_scheme = path.split("://", 1)[1]
        slash = no_scheme.find("/")
        path = no_scheme[slash:] if slash >= 0 else "/"
    if "?" in path:
        path = path.split("?", 1)[0]

    query = []
    for q in url.get("query", []) or []:
        if not isinstance(q, dict):
            continue
        query.append({
            "key": q.get("key", ""),
            "value": q.get("value", ""),
            "description": _description(q.get("description")),
            "disabled": q.get("disabled", False),
        })

    # Path parameters: either :foo or {foo}
    path_params = re.findall(r":(\w+)|\{(\w+)\}", path)
    path_params = [a or b for a, b in path_params]

    return path, query, path_params


def _parse_body(body: Any) -> tuple[str | None, dict[str, Any] | None]:
    """Return the body as (type, schema)."""
    if not isinstance(body, dict):
        return None, None

    mode = body.get("mode")
    if mode == "raw":
        raw = body.get("raw", "")
        if not raw.strip():
            return None, None
        try:
            parsed = json.loads(raw)
            if isinstance(parsed, dict):
                # Infer field types
                schema = {}
                for k, v in parsed.items():
                    schema[k] = _infer_type(v)
                return "json", schema
            elif isinstance(parsed, list):
                return "json_array", {"_items": _infer_type(parsed[0]) if parsed else "Any"}
        except json.JSONDecodeError:
            return "raw", None
        return "raw", None
    if mode == "formdata":
        schema = {}
        for f in body.get("formdata", []):
            if isinstance(f, dict):
                schema[f.get("key", "")] = "str"
        return "formdata", schema
    if mode == "urlencoded":
        schema = {}
        for f in body.get("urlencoded", []):
            if isinstance(f, dict):
                schema[f.get("key", "")] = "str"
        return "urlencoded", schema
    if mode == "file":
        return "file", None
    return None, None


def _infer_type(value: Any) -> str:
    if isinstance(value, bool):
        return "bool"
    if isinstance(value, int):
        return "int"
    if isinstance(value, float):
        return "float"
    if isinstance(value, str):
        return "str"
    if isinstance(value, list):
        if value:
            return f"list[{_infer_type(value[0])}]"
        return "list"
    if isinstance(value, dict):
        return "dict"
    if value is None:
        return "Any | None"
    return "Any"


def walk(items: list[dict], category: str = "", subcategory: str = "", depth: int = 0) -> list[Endpoint]:
    """Walk the Postman item tree and produce a list of Endpoints."""
    out: list[Endpoint] = []
    for it in items:
        name = it.get("name", "")
        if "request" in it:
            req = it["request"]
            if not isinstance(req, dict):
                continue
            path, query, path_params = _parse_url(req.get("url"))
            body_type, body_schema = _parse_body(req.get("body"))
            out.append(Endpoint(
                name=name,
                method=req.get("method", "GET"),
                path=path,
                category=category,
                subcategory=subcategory,
                query_params=query,
                path_params=path_params,
                body_schema=body_schema,
                body_type=body_type,
                description=_description(req.get("description")),
            ))
        else:
            if depth == 0:
                out.extend(walk(it.get("item", []), category=name, depth=1))
            elif depth == 1:
                out.extend(walk(it.get("item", []), category=category, subcategory=name, depth=2))
            else:
                # Deeper levels — collect subfolders under the current category
                out.extend(walk(it.get("item", []), category=category, subcategory=subcategory, depth=depth+1))
    return out


def load_endpoints(postman_json: Path) -> list[Endpoint]:
    data = json.loads(postman_json.read_text())
    return walk(data.get("item", []))
