# Publishing

Configure a PyPI pending Trusted Publisher at https://pypi.org/manage/account/publishing/:

- PyPI project: `genpark-financial-audit`
- GitHub owner: `Alpha-Park`
- Repository: `genpark-complex-financial-formula-audit-validator-skill`
- Workflow: `publish-pypi.yml`
- Environment: `pypi`

After configuring the publisher, run **Actions -> Publish PyPI -> Run workflow** at the reviewed commit.
This uses GitHub OIDC; do not commit an API token. Existing versions cannot be overwritten on PyPI.
Verify the PyPI project and install in a fresh environment before marking it published.

The official MCP Registry can also distribute the GitHub release MCPB independently of PyPI.
Smithery supports MCPB publishing, but requires an authenticated Smithery account.
PulseMCP reported submissions paused when checked on 2026-09-28.

After setup, publishing a new GitHub Release triggers the same build/test/PyPI workflow automatically. Bump pyproject.toml before releasing a new version.

## Verified MCP Registry publication

Version 1.0.1 is active in the [official MCP Registry](https://registry.modelcontextprotocol.io/v0.1/servers/io.github.Alpha-Park%2Fgenpark-financial-audit/versions/1.0.1).
The public MCPB download was retrieved and its SHA-256 matched the registry metadata.
PyPI and Smithery remain pending authentication/configuration.
