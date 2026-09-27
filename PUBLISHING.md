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
