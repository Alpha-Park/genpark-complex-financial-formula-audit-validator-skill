import json
import subprocess
import sys
import unittest
from pathlib import Path

class ProtocolTests(unittest.TestCase):
    def test_notifications_errors_and_schema(self):
        messages = [
            {"jsonrpc":"2.0","method":"notifications/initialized"},
            {"jsonrpc":"2.0","id":1,"method":"unknown"},
            {"jsonrpc":"2.0","id":2,"method":"tools/call","params":{"name":"unknown"}},
            {"jsonrpc":"2.0","id":3,"method":"tools/list"},
        ]
        proc = subprocess.run([sys.executable,str(Path(__file__).resolve().parents[1]/"mcp_server.py")],input="\n".join(json.dumps(m) for m in messages)+"\n{bad}\n",text=True,capture_output=True,timeout=15,check=True)
        replies = [json.loads(x) for x in proc.stdout.splitlines()]
        self.assertEqual(len(replies),4)
        self.assertEqual(replies[0]["error"]["code"],-32601)
        self.assertEqual(replies[1]["error"]["code"],-32602)
        self.assertEqual(replies[3]["error"]["code"],-32700)
        self.assertEqual(len(replies[2]["result"]["tools"]),4)
