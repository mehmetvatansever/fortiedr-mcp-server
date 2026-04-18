"""Mock-HTTP tests for FortiEDRClient.

Uses httpx.MockTransport to exercise client behaviour without any real network.
"""
from __future__ import annotations

import httpx
import pytest

from fortiedr_mcp.client import FortiEDRClient, FortiEDRError


@pytest.mark.asyncio
async def test_get_returns_json():
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(200, json={"status": True, "data": [1, 2, 3]})

    transport = httpx.MockTransport(handler)
    client = FortiEDRClient(host="edr.test", user="u", password="p")
    # inject the transport (normally __aenter__ builds the AsyncClient)
    client._client = httpx.AsyncClient(transport=transport, base_url="https://edr.test")
    try:
        result = await client.get("/management-rest/events/list-events")
        assert result == {"status": True, "data": [1, 2, 3]}
    finally:
        await client._client.aclose()


@pytest.mark.asyncio
async def test_4xx_raises_fortiedr_error():
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(401, json={"error": "Unauthorized"})

    transport = httpx.MockTransport(handler)
    client = FortiEDRClient(host="edr.test", user="u", password="p", max_retries=0)
    client._client = httpx.AsyncClient(transport=transport, base_url="https://edr.test")
    try:
        with pytest.raises(FortiEDRError) as exc_info:
            await client.get("/management-rest/something")
        assert exc_info.value.status_code == 401
    finally:
        await client._client.aclose()


@pytest.mark.asyncio
async def test_org_injected_as_query_param():
    captured = {}

    def handler(request: httpx.Request) -> httpx.Response:
        captured["url"] = str(request.url)
        return httpx.Response(200, json={})

    transport = httpx.MockTransport(handler)
    client = FortiEDRClient(
        host="edr.test", user="u", password="p", default_org="ACME Corp"
    )
    client._client = httpx.AsyncClient(transport=transport, base_url="https://edr.test")
    try:
        await client.get("/management-rest/events/list-events")
        assert "organization=ACME" in captured["url"].replace("+", " ").replace("%20", " ")
    finally:
        await client._client.aclose()


@pytest.mark.asyncio
async def test_explicit_org_overrides_default():
    captured = {}

    def handler(request: httpx.Request) -> httpx.Response:
        captured["url"] = str(request.url)
        return httpx.Response(200, json={})

    transport = httpx.MockTransport(handler)
    client = FortiEDRClient(
        host="edr.test", user="u", password="p", default_org="ACME"
    )
    client._client = httpx.AsyncClient(transport=transport, base_url="https://edr.test")
    try:
        await client.get("/events", organization="OtherCorp")
        assert "OtherCorp" in captured["url"].replace("+", " ").replace("%20", " ")
        assert "ACME" not in captured["url"]
    finally:
        await client._client.aclose()
