"""Configuration for FortiEDR MCP server.

All configuration comes from environment variables so local stdio and
Docker/HTTP deployments run on the same code path.
"""
from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Config:
    host: str
    user: str
    password: str
    default_org: str | None
    enable_destructive: bool
    read_only: bool
    verify_ssl: bool
    expose_raw_api: bool

    @classmethod
    def from_env(cls) -> "Config":
        host = os.getenv("FORTIEDR_HOST", "").strip()
        user = os.getenv("FORTIEDR_USER", "").strip()
        password = os.getenv("FORTIEDR_PASSWORD", "")
        default_org = os.getenv("FORTIEDR_DEFAULT_ORG") or None
        enable_destructive = _bool_env("FORTIEDR_ENABLE_DESTRUCTIVE", default=False)
        read_only = _bool_env("FORTIEDR_READ_ONLY", default=False)
        verify_ssl = _bool_env("FORTIEDR_VERIFY_SSL", default=True)
        expose_raw_api = _bool_env("FORTIEDR_EXPOSE_RAW_API", default=False)

        missing = [k for k, v in {
            "FORTIEDR_HOST": host,
            "FORTIEDR_USER": user,
            "FORTIEDR_PASSWORD": password,
        }.items() if not v]
        if missing:
            raise RuntimeError(
                f"Missing environment variables: {', '.join(missing)}. "
                "Check your .env file or your Claude Desktop/VS Code config."
            )

        return cls(
            host=host,
            user=user,
            password=password,
            default_org=default_org,
            enable_destructive=enable_destructive,
            read_only=read_only,
            verify_ssl=verify_ssl,
            expose_raw_api=expose_raw_api,
        )


def _bool_env(name: str, default: bool) -> bool:
    raw = os.getenv(name)
    if raw is None:
        return default
    return raw.strip().lower() in {"1", "true", "yes", "on"}
