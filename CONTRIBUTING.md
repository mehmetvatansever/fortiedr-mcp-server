# Contributing guide

## Development setup

```bash
git clone https://github.com/YOUR-ORG/fortiedr-mcp.git
cd fortiedr-mcp
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

## Adding a new tool

1. Create a new module under `src/fortiedr_mcp/tools/` or extend an
   existing one.
2. Add a new `@mcp.tool()`-decorated function inside the appropriate
   `register_read`, `register_write`, or `register_destructive` function.
3. Write the **docstring** carefully — Claude relies on it when picking
   a tool. Keep it clear and consistent.
4. Don't forget the `organization: str | None = None` parameter.
5. Put `auth.ensure(organization)` at the top of the function.

## Tests

```bash
pytest
ruff check src/
mypy src/
```

## Action categorisation

When deciding which category a new tool belongs to:

- **read**: Returns data only, does not change FortiEDR state
- **write**: Changes state but does not touch endpoints (classify, comment, policy assignment)
- **destructive**: Changes endpoint behaviour (isolate, remove collector, execute remediation)

When in doubt, move it up one category.

## PR workflow

1. Open an issue or pick an existing one
2. Create a feature branch (`feat/add-xyz-tool`)
3. Make the change, add tests, ensure `ruff` and `mypy` are clean
4. Open a PR and reference the issue number
