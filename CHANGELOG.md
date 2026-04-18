# Changelog

This file follows the [Keep a Changelog](https://keepachangelog.com/) format.
Versioning follows [SemVer](https://semver.org/).

## [0.1.0] - 2026-04-17

First open-source release.

### Architecture

- Async HTTP client (httpx-based) — no dependency on the `fortiedr` Python SDK
- Three-layer tool registry: `_generated/` → `curated/` → `composite/`
- Override pattern: curated/composite modules can hide tools in the generated layer
- Mode-based registration: read-only / standard / destructive

### API coverage

- 146 FortiEDR endpoints exposed as auto-generated tools (`_generated/`)
- 25 modules grouped by category: events, inventory, threat-hunting, policies,
  integrations, organizations, audit, iot, forensics, exceptions, etc.

### Curated (hand-polished) tools

- `events_list_events`, `events_count_events`, `events_list_raw_data_items`,
  `events_update` — enriched docstrings, smarter parameters
- `threat_hunting_search`, `threat_hunting_facets`, `threat_hunting_counts`
  — docstrings full of query-language examples
- `inventory_list_collectors`, `inventory_isolate_collectors`,
  `inventory_unisolate_collectors` — safety warnings for destructive actions

### Composite tools

- `mssp_event_summary_by_org` — pulls event counts across all tenants in parallel
- `mssp_ioc_sweep` — sweeps for an IoC across the fleet
- `mdr_event_triage_brief` — assembles event + raw data + exceptions for FP/TP decisions
- `mdr_monthly_report_data` — gathers all data needed for a monthly customer report

### Generator tooling

- `tools/postman_parser.py` — extracts endpoint metadata from the Postman collection
- `tools/gen_api_reference.py` — emits the API reference markdown
- `tools/gen_tools.py` — emits the MCP tool stubs

### Deployment

- stdio and HTTP (streamable-http) transports
- Dockerfile (multi-stage, non-root user, healthcheck)
- GitHub Actions CI (Python 3.10/3.11/3.12)
- GitHub Actions Docker workflow (multi-arch image pushed to GHCR)
- Sample configs for Claude Desktop, Cursor, VS Code + Copilot, Claude Code

### Documentation

- Professional README (architecture diagram, example workflows, badges)
- `docs/api-reference.md` — reference for all 146 endpoints
- `docs/mssp-guide.md` — MSSP/MDR deployment guide
- `CONTRIBUTING.md` — guide for adding new tools
