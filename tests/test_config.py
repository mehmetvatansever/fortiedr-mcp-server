"""Smoke tests for Config and AuthManager."""
from __future__ import annotations

import pytest

from fortiedr_mcp.auth import AuthManager
from fortiedr_mcp.config import Config


def test_config_requires_mandatory_fields(monkeypatch):
    for var in ["FORTIEDR_HOST", "FORTIEDR_USER", "FORTIEDR_PASSWORD"]:
        monkeypatch.delenv(var, raising=False)

    with pytest.raises(RuntimeError, match="Missing environment"):
        Config.from_env()


def test_config_defaults(monkeypatch):
    monkeypatch.setenv("FORTIEDR_HOST", "edr.test")
    monkeypatch.setenv("FORTIEDR_USER", "u")
    monkeypatch.setenv("FORTIEDR_PASSWORD", "p")
    for var in ("FORTIEDR_DEFAULT_ORG", "FORTIEDR_READ_ONLY",
                "FORTIEDR_ENABLE_DESTRUCTIVE", "FORTIEDR_VERIFY_SSL"):
        monkeypatch.delenv(var, raising=False)

    cfg = Config.from_env()
    assert cfg.host == "edr.test"
    assert cfg.default_org is None
    assert cfg.enable_destructive is False
    assert cfg.read_only is False
    assert cfg.verify_ssl is True


def test_config_bool_parsing(monkeypatch):
    monkeypatch.setenv("FORTIEDR_HOST", "edr.test")
    monkeypatch.setenv("FORTIEDR_USER", "u")
    monkeypatch.setenv("FORTIEDR_PASSWORD", "p")
    monkeypatch.setenv("FORTIEDR_READ_ONLY", "true")
    monkeypatch.setenv("FORTIEDR_ENABLE_DESTRUCTIVE", "yes")
    monkeypatch.setenv("FORTIEDR_VERIFY_SSL", "0")

    cfg = Config.from_env()
    assert cfg.read_only is True
    assert cfg.enable_destructive is True
    assert cfg.verify_ssl is False


def test_auth_resolve_org_with_default(monkeypatch):
    monkeypatch.setenv("FORTIEDR_HOST", "edr.test")
    monkeypatch.setenv("FORTIEDR_USER", "u")
    monkeypatch.setenv("FORTIEDR_PASSWORD", "p")
    monkeypatch.setenv("FORTIEDR_DEFAULT_ORG", "ACME Corp")

    cfg = Config.from_env()
    auth = AuthManager(cfg)
    assert auth.resolve_org() == "ACME Corp"
    assert auth.resolve_org("Other Inc") == "Other Inc"
    assert auth.ensure() == "ACME Corp"


def test_auth_resolve_org_without_default(monkeypatch):
    monkeypatch.setenv("FORTIEDR_HOST", "edr.test")
    monkeypatch.setenv("FORTIEDR_USER", "u")
    monkeypatch.setenv("FORTIEDR_PASSWORD", "p")
    monkeypatch.delenv("FORTIEDR_DEFAULT_ORG", raising=False)

    cfg = Config.from_env()
    auth = AuthManager(cfg)
    assert auth.resolve_org() is None
    assert auth.resolve_org("X") == "X"
