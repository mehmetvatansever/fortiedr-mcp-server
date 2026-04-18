"""FortiEDR authentication and multi-org context management.

No longer depends on the fortiedr SDK — uses a pure HTTP client instead.
AuthManager only holds config and provides the shared state used by tools.
The actual authentication is sent by FortiEDRClient as a basic auth header
on every request.
"""
from __future__ import annotations

import logging
from threading import Lock

from .config import Config

log = logging.getLogger(__name__)


class AuthManager:
    """Carrier for config and organization context shared across tools.

    Since the HTTP client sends basic auth on every request, there is no
    concept of "login" here; this class only holds the default org and
    config, and could later be used to cache session tokens if needed.
    """

    def __init__(self, cfg: Config) -> None:
        self._cfg = cfg
        self._lock = Lock()

    @property
    def config(self) -> Config:
        return self._cfg

    def resolve_org(self, org: str | None = None) -> str | None:
        """Return the requested org, or the default."""
        return org or self._cfg.default_org

    def ensure(self, org: str | None = None) -> str | None:
        """Backwards-compatible alias for resolve_org."""
        return self.resolve_org(org)
