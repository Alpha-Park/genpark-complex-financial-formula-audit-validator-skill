# genpark-financial-audit

Arithmetic consistency checks for supplied financial statement data.

This checks supplied numbers and a simplified income-statement model. It does not extract PDFs, verify source authenticity, check accounting compliance, or provide an audit opinion. Monetary values must use consistent units; tolerance defaults to 0.5 of those units.

## Install from the GitHub release

Python 3.9 or newer. The library and stdio MCP server have no runtime dependencies.

```sh
python -m pip install https://github.com/Alpha-Park/genpark-complex-financial-formula-audit-validator-skill/releases/download/v1.0.1/genpark_financial_audit-1.0.1-py3-none-any.whl
```

PyPI publication is pending account setup. The intended PyPI project is `genpark-financial-audit`;
do not assume `pip install genpark-financial-audit` is available until the project is published.

## Python usage

```python
from genpark_financial_audit import FinancialFormulaAuditValidator
client = FinancialFormulaAuditValidator()
print(client.run_benchmark_financial_audit())
```

## MCP stdio configuration

After installing the wheel, configure your MCP client with the installed command:

```json
{
  "mcpServers": {
    "genpark-financial-audit": {
      "command": "genpark-financial-audit",
      "args": []
    }
  }
}
```

If the command is not on PATH, use its absolute path or `python -m genpark_financial_audit`
with the same interpreter where you installed the wheel.
The GitHub release also contains a `.mcpb` bundle for clients supporting desktop extensions.
That bundle requires a Python 3.9+ interpreter on PATH; it bundles the server source.

Available tools: `audit_balance_sheet`, `audit_income_statement`, `audit_cross_footing`, `run_benchmark_financial_audit`.
`tools/list` returns required arguments and JSON schemas.
Each MCP process holds its own state. Benchmark tools use isolated instances.

## Development

```sh
python -m unittest discover -s tests
python -m pip install mcp
python tests/check_mcp.py
python -m pip install build twine
python -m build
python -m twine check dist/*
```

`python mcp_server.py --test` runs the deterministic example; it is not a protocol conformance test.
The MCP client check exercises initialize, tools/list, tools/call and ping over stdio.

## Distribution

GitHub source and release artifacts are the primary distribution until PyPI is configured.
Registry submissions are tracked separately; a manifest is not proof of registry acceptance.
See [PUBLISHING.md](PUBLISHING.md) for the repeatable PyPI workflow.

MIT license. Maintained by [GenPark](https://genpark.ai).

<!-- mcp-name: io.github.Alpha-Park/genpark-financial-audit -->
