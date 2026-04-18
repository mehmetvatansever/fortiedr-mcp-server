# MSSP / MDR Usage Guide

This guide explains how to run the FortiEDR MCP safely in an MSSP or MDR
environment.

## Recommended deployment topology

Rather than a single "everyone uses it" MCP, we recommend
**role-based separate deployments**:

### 1. Reporting instance (read-only)

```bash
FORTIEDR_READ_ONLY=true
FORTIEDR_ENABLE_DESTRUCTIVE=false
```

- Open to all analysts, managers, and anyone drafting customer reports
- Risk: none, read-only
- Use: triage, hunting, reporting, dashboards

### 2. Tier 1 analyst instance (writes allowed, no isolation)

```bash
FORTIEDR_READ_ONLY=false
FORTIEDR_ENABLE_DESTRUCTIVE=false
```

- Can classify, handle, comment
- Cannot isolate
- Risk: low (can change event status but cannot touch endpoints)

### 3. Senior analyst / IR instance (full privileges)

```bash
FORTIEDR_READ_ONLY=false
FORTIEDR_ENABLE_DESTRUCTIVE=true
```

- Everything enabled, including isolation
- Open only to senior analysts and the IR team
- Risk: high — misuse causes customer business disruption

## Multi-tenant safety principles

### Principle 1: Make the org parameter mandatory

Defining a default org is convenient but risky. To prevent the
"isolated the wrong customer's machine" scenario:

- Do **not** set `FORTIEDR_DEFAULT_ORG`
- Require the analyst to state which customer they are working on in
  every prompt
- For destructive operations, use a system prompt that makes Claude ask
  "which org, which device?" and wait for confirmation

### Principle 2: Audit trail

On every write, put metadata in the comment field in this format:

```
AI-assisted via FortiEDR MCP | analyst: <name> | ticket: <ID> | model: <model-name>
```

This lets you answer "who closed this event and why" during an audit six
months later.

### Principle 3: Customer data residency

Cloud-hosted clients like Claude.ai, Cursor, and Copilot send FortiEDR
data to Anthropic/Microsoft/the vendor. In your customer contracts:

- Is the data-processing addendum (DPA) up to date?
- Is AI tool usage explicitly covered?
- For regulated-sector customers (finance, healthcare, public sector),
  is there an opt-out?

For regulation-sensitive customers, use **Claude API + Zero Data Retention**
or an on-premise LLM.

## Typical workflows

### Morning triage (3 minutes instead of 15)

```
"Use list_organizations() to get every customer.
For each customer, count events with severity=Critical or High and
handled=false over the last 8 hours. Show a table of customer + count,
sorted by highest count first."
```

### Monthly customer report

```
"For ACME Corp between 2026-03-01 and 2026-03-31:
- Total event count, severity breakdown
- The 10 endpoints with the most events
- Classification breakdown
- Events still open
Produce the output as a docx."
```

### Cross-tenant threat hunting

```
"Search for process-creation events containing 'powershell.exe -enc'
across every tenant over the last 7 days. For each customer show the
number of results plus the oldest/newest timestamps in a table."
```

### FP triage assistant (human-approved)

```
"Analyse event ID 12345:
- Use get_event_raw_data to pull the process chain
- Summarise the hash and signer
- Use list_exceptions to check whether a similar exception exists
- Write an FP/TP recommendation with a confidence score, but do not act"
```

The analyst reads the recommendation and, if they approve, calls
`update_events` to close the event. Claude never auto-closes FPs.

## Suggested system prompt (Claude Desktop project instructions)

```
You are an assistant helping an MDR SOC analyst. You have access to the
FortiEDR MCP tools.

RULES:
1. This is a multi-tenant environment. Before any write or destructive
   operation, you MUST ask "which customer (organization) is this for?".
2. When calling update_events, always put
   "AI-assisted, analyst: <name>, session: <datetime>" in the comment field.
3. Never call isolate_collectors without approval. State the affected
   device and customer first, and only call it after the analyst says
   "yes, isolate".
4. Always provide FP/TP recommendations with a confidence score and
   justification. Do not close an event without analyst approval.
5. Do not include sensitive customer data (usernames, IPs) in responses
   unless strictly necessary.
```
