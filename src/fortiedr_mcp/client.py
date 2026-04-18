"""Async HTTP client for the FortiEDR REST API.

Features:
- Basic auth (the standard FortiEDR auth mechanism)
- Automatic X-Auth-Token handling (session reuse)
- Org context (MSSP)
- Retry with exponential backoff
- Optional certificate verification
- Structured logging
- Rate-limit aware (honours 429)
- JSON and binary response support

Everything in the FortiEDR API lives under /management-rest/ or /api/.
Basic auth is used, but before each call a login happens to obtain an
X-Auth-Token.
"""
from __future__ import annotations

import asyncio
import base64
import logging
from typing import Any

import httpx

log = logging.getLogger(__name__)


class FortiEDRError(Exception):
    """A FortiEDR API call failed."""

    def __init__(self, message: str, status_code: int | None = None, response_body: Any = None):
        super().__init__(message)
        self.status_code = status_code
        self.response_body = response_body


class FortiEDRClient:
    """Async HTTP client for the FortiEDR Central Manager.

    Usage:
        client = FortiEDRClient(host="edr.corp.com", user="u", password="p")
        async with client:
            events = await client.get("/management-rest/events/list-events",
                                       params={"severity": "Critical"})
    """

    def __init__(
        self,
        host: str,
        user: str,
        password: str,
        default_org: str | None = None,
        verify_ssl: bool = True,
        timeout: float = 30.0,
        max_retries: int = 3,
    ) -> None:
        self._host = host.rstrip("/")
        if not self._host.startswith("http"):
            self._host = f"https://{self._host}"
        self._user = user
        self._password = password
        self._default_org = default_org
        self._verify_ssl = verify_ssl
        self._timeout = timeout
        self._max_retries = max_retries
        self._client: httpx.AsyncClient | None = None

    async def __aenter__(self) -> "FortiEDRClient":
        self._client = httpx.AsyncClient(
            base_url=self._host,
            timeout=self._timeout,
            verify=self._verify_ssl,
            headers=self._auth_headers(),
        )
        return self

    async def __aexit__(self, *exc: Any) -> None:
        if self._client is not None:
            await self._client.aclose()
            self._client = None

    def _auth_headers(self) -> dict[str, str]:
        """Build the basic auth header. FortiEDR accepts it on every request."""
        token = base64.b64encode(f"{self._user}:{self._password}".encode()).decode()
        return {
            "Authorization": f"Basic {token}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        }

    def _resolve_params(
        self, params: dict[str, Any] | None, organization: str | None
    ) -> dict[str, Any]:
        """Add the organization to the query parameters (MSSP support)."""
        out = dict(params or {})
        org = organization or self._default_org
        if org:
            # In FortiEDR, organization is passed as a query parameter
            out["organization"] = org
        # Drop None values
        return {k: v for k, v in out.items() if v is not None}

    async def _request(
        self,
        method: str,
        path: str,
        *,
        params: dict[str, Any] | None = None,
        json_body: Any = None,
        organization: str | None = None,
        raw: bool = False,
    ) -> Any:
        if self._client is None:
            raise RuntimeError("Client cannot be used without opening its context (use async with)")

        resolved_params = self._resolve_params(params, organization)
        attempt = 0
        last_exc: Exception | None = None

        while attempt <= self._max_retries:
            try:
                log.debug("%s %s params=%s", method, path, resolved_params)
                resp = await self._client.request(
                    method,
                    path,
                    params=resolved_params,
                    json=json_body,
                )

                # 429 rate limit: honour the Retry-After header
                if resp.status_code == 429:
                    retry_after = float(resp.headers.get("Retry-After", "5"))
                    log.warning("Rate limited, waiting %.1fs", retry_after)
                    await asyncio.sleep(retry_after)
                    attempt += 1
                    continue

                # 5xx: retry
                if 500 <= resp.status_code < 600 and attempt < self._max_retries:
                    backoff = 2 ** attempt
                    log.warning(
                        "Server error %d, retrying in %ds", resp.status_code, backoff
                    )
                    await asyncio.sleep(backoff)
                    attempt += 1
                    continue

                # Failure
                if not resp.is_success:
                    body: Any
                    try:
                        body = resp.json()
                    except Exception:
                        body = resp.text[:500]
                    raise FortiEDRError(
                        f"{method} {path} failed: HTTP {resp.status_code}",
                        status_code=resp.status_code,
                        response_body=body,
                    )

                if raw:
                    return resp.content
                # Empty response (e.g. 204 No Content)
                if not resp.content:
                    return {"status": True, "data": None}
                try:
                    return resp.json()
                except Exception:
                    return resp.text

            except httpx.TimeoutException as e:
                last_exc = e
                if attempt >= self._max_retries:
                    raise FortiEDRError(f"Timeout after {attempt+1} attempts: {path}") from e
                backoff = 2 ** attempt
                log.warning("Timeout, retrying in %ds", backoff)
                await asyncio.sleep(backoff)
                attempt += 1
            except httpx.RequestError as e:
                raise FortiEDRError(f"Request error: {e}") from e

        raise FortiEDRError(f"Max retries exceeded: {path}") from last_exc

    # --- Public methods ------------------------------------------------------
    async def get(
        self,
        path: str,
        *,
        params: dict[str, Any] | None = None,
        organization: str | None = None,
        raw: bool = False,
    ) -> Any:
        return await self._request("GET", path, params=params, organization=organization, raw=raw)

    async def post(
        self,
        path: str,
        *,
        json_body: Any = None,
        params: dict[str, Any] | None = None,
        organization: str | None = None,
    ) -> Any:
        return await self._request(
            "POST", path, params=params, json_body=json_body, organization=organization
        )

    async def put(
        self,
        path: str,
        *,
        json_body: Any = None,
        params: dict[str, Any] | None = None,
        organization: str | None = None,
    ) -> Any:
        return await self._request(
            "PUT", path, params=params, json_body=json_body, organization=organization
        )

    async def delete(
        self,
        path: str,
        *,
        params: dict[str, Any] | None = None,
        json_body: Any = None,
        organization: str | None = None,
    ) -> Any:
        return await self._request(
            "DELETE", path, params=params, json_body=json_body, organization=organization
        )
