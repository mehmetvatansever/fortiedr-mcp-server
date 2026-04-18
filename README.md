# FortiEDR MCP Server

[![CI](https://github.com/mehmetvatansever/fortiedr-mcp-server/actions/workflows/ci.yml/badge.svg)](https://github.com/mehmetvatansever/fortiedr-mcp-server/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![MCP](https://img.shields.io/badge/MCP-compatible-green.svg)](https://modelcontextprotocol.io)

**Model Context Protocol server for Fortinet FortiEDR.** Works with Claude,
Cursor, VS Code + Copilot, Windsurf, Claude Code — same server everywhere.

Designed specifically for **MDR / MSSP** operations: multi-tenant support,
read-only mode, explicit opt-in for destructive actions, and composite tools
that sweep every tenant from a single prompt.

## Why this MCP?

```
Scenario: 09:00 stand-up with 35 MSSP customers on your plate.
"Summarise the last 8 hours of handled=false critical events across all tenants."
```

The old way: open 35 tabs, filter each one, take notes → ~45 minutes.
With this MCP: a single prompt, 30 seconds.

```
Scenario: CISA has just published a new APT hash.
"Sweep for this hash across every tenant over the last 30 days."
```

The old way: open the threat-hunting tab per customer, copy the query → 30 min.
With this MCP: a single `mssp_ioc_sweep` call, in parallel.

## Features

### 146 FortiEDR API endpoints

Auto-generated from the official FortiEDR Postman collection. Grouped by
category — events, inventory, threat hunting, policies, integrations,
organizations, audit, and more.

### MSSP composite tools

Combine several endpoints into tools that produce real business value:

| Tool | What it does |
|------|--------------|
| `mssp_event_summary_by_org` | Pulls event counts across all tenants in parallel and ranks them |
| `mssp_ioc_sweep` | Sweeps for an IoC (hash/IP/domain) across the fleet |
| `mdr_event_triage_brief` | Assembles all context needed to make an FP/TP decision for an event |
| `mdr_monthly_report_data` | Gathers every piece of data needed for a monthly customer report in a single call |

### Three safety modes

| Mode | READ_ONLY | DESTRUCTIVE | Use case |
|---|---|---|---|
| **Safe** | `true` | - | Reporting, hunting. Recommended for production. |
| **Standard** | `false` | `false` | Classify, comment, policy. Tier 1 analyst. |
| **Full** | `false` | `true` | Everything including isolation. Senior / IR team. |

### Modern async stack

httpx-based HTTP client with retry, rate limit, and timeout handling.
No dependency on the `fortiedr` Python SDK — talks to the REST API directly.

## Quick start

### 1. Prep on the FortiEDR side

Central Manager > Administration > Users → new user, role:
**Rest API** (the Admin role on its own is **not** enough).

After creating the account, log in to the console once with it and rotate
the password. Skip this step and the API will return 401.

### 2. Install

```bash
git clone https://github.com/mehmetvatansever/fortiedr-mcp-server.git
cd fortiedr-mcp-server
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -e .
cp .env.example .env              # edit it
```

### 3. Test

```bash
# Does it run?
python -m fortiedr_mcp

# Interactive debug:
npx @modelcontextprotocol/inspector python -m fortiedr_mcp
```

## Wiring into your client

### Claude Desktop

`~/Library/Application Support/Claude/claude_desktop_config.json` (macOS) or
`%APPDATA%\Claude\claude_desktop_config.json` (Windows):

```json
{
  "mcpServers": {
    "fortiedr": {
      "command": "/absolute/path/.venv/bin/python",
      "args": ["-m", "fortiedr_mcp"],
      "env": {
        "FORTIEDR_HOST": "edr.your-company.com",
        "FORTIEDR_USER": "api_user",
        "FORTIEDR_PASSWORD": "change-me",
        "FORTIEDR_READ_ONLY": "true"
      }
    }
  }
}
```

See `examples/` for other clients (Cursor, VS Code, Claude Code).

### Docker (HTTP transport)

```bash
docker run -d --name fortiedr-mcp \
  -p 3000:3000 \
  -e FORTIEDR_HOST=edr.your-company.com \
  -e FORTIEDR_USER=api_user \
  -e FORTIEDR_PASSWORD=change-me \
  -e FORTIEDR_READ_ONLY=true \
  ghcr.io/mehmetvatansever/fortiedr-mcp-server:latest
```

Then use the HTTP transport in your client config:

```json
{
  "mcpServers": {
    "fortiedr": {
      "type": "http",
      "url": "http://localhost:3000/mcp"
    }
  }
}
```

## Architecture

```
┌──────────────────────────────────────────────────────┐
│  MCP client (Claude / Cursor / VS Code / Windsurf)   │
└────────────────────────┬─────────────────────────────┘
                         │ stdio or HTTP
┌────────────────────────▼─────────────────────────────┐
│                 server.py                            │
│  • Config loading                                    │
│  • Mode-based tool registration                      │
└────────────────────────┬─────────────────────────────┘
                         │
         ┌───────────────┼───────────────┐
         ▼               ▼               ▼
┌────────────────┐ ┌──────────┐ ┌────────────────┐
│  _generated/   │ │ curated/ │ │  composite/    │
│  146 endpoints │ │ polished │ │  MSSP / MDR    │
│  auto-gen      │ │ versions │ │  business tools│
└────────┬───────┘ └────┬─────┘ └────────┬───────┘
         │              │                │
         └──────────────┼────────────────┘
                        ▼
              ┌──────────────────┐
              │  client.py       │  (async httpx)
              │  • Basic auth    │
              │  • Retry/429     │
              │  • Org context   │
              └─────────┬────────┘
                        ▼
              ┌──────────────────┐
              │ FortiEDR REST API│
              └──────────────────┘
```

### Override pattern

`curated/` and `composite/` modules declare an `OVERRIDES` set to hide
same-named tools in `_generated/`. This lets you add hand-polished versions
on top of the auto-generated stubs without touching them.

```python
# curated/events.py
OVERRIDES = {"events_list_events", "events_count_events"}

def register_read(mcp, auth):
    @mcp.tool(name="events_list_events")
    async def events_list_events(...):
        """Polished docstring, smarter parameters..."""
```

## Example usage

### Morning triage

> **You:** Summarise the handled=false critical and high events across every tenant over the last 8 hours, grouped by customer.
>
> **Claude:** *Calls `mssp_event_summary_by_org`, presents the result as a table.*

### IoC sweep

> **You:** Search for hash `abc123...` across every tenant over the last 30 days.
>
> **Claude:** *Calls `mssp_ioc_sweep`, reports the affected customers.*

### FP triage assistant

> **You:** Analyse event 12345, suggest FP vs TP, but don't take action.
>
> **Claude:** *Uses `mdr_event_triage_brief` to assemble context, writes a reasoned recommendation based on the process chain and hash — leaves the decision to you.*

### Monthly report

> **You:** Produce the March report for ACME Corp as a docx.
>
> **Claude:** *Pulls everything through `mdr_monthly_report_data`, formats it via the docx skill.*

## MSSP deployment guide

[docs/mssp-guide.md](docs/mssp-guide.md) — safe deployment topology, audit
trail approach, customer data-residency considerations.

## API reference

[docs/api-reference.md](docs/api-reference.md) — categorised reference of all
146 endpoints, auto-generated from the Postman collection.

## Development

```bash
pip install -e ".[dev]"

# Test
pytest tests/ -v

# Lint
ruff check src/ tests/ tools/

# Refresh the API reference (after the Postman collection changes)
python tools/gen_api_reference.py \
  fortiedr_api.postman_collection.json \
  docs/api-reference.md

# Refresh generated tools (after new endpoints are added)
python tools/gen_tools.py \
  fortiedr_api.postman_collection.json \
  src/fortiedr_mcp/tools/_generated
```

[CONTRIBUTING.md](CONTRIBUTING.md) — adding new tools, PR process.

## Security

Open an [issue](../../issues) for bugs and security vulnerabilities.
Recommendations for production deployment:

- Start with `FORTIEDR_READ_ONLY=true`
- Only expose destructive tools to senior analysts
- Put audit metadata into the comment field when calling `update_events`
- In MSSP environments do not set `FORTIEDR_DEFAULT_ORG` — require the org on every call

## License

[MIT](LICENSE).

## Disclaimer

This project is not affiliated with Fortinet Inc. FortiEDR and Fortinet are
trademarks of Fortinet Inc. Test in your own environment and use at your own
risk and responsibility.
