import asyncio
import json
import sys
from pathlib import Path
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def check():
    root = Path(__file__).resolve().parents[1]
    params = StdioServerParameters(command=sys.executable, args=[str(root / "mcp_server.py")])
    async with stdio_client(params) as (read, write):
        async with ClientSession(read, write) as session:
            init = await session.initialize()
            assert init.serverInfo.name == "genpark-financial-audit"
            tools = await session.list_tools()
            assert len(tools.tools) == 4
            assert all(t.inputSchema.get("type") == "object" for t in tools.tools)
            await session.send_ping()
            result = await session.call_tool("run_benchmark_financial_audit", {})
            assert not result.isError
            assert json.loads(result.content[0].text)["benchmark_status"] == "PASSED"
    print("PASS official MCP client initialize/list/call/ping: genpark-financial-audit")

asyncio.run(check())
