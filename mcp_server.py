import sys, json
from client import FinancialFormulaAuditValidator

def main():
    validator = FinancialFormulaAuditValidator()
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        print(json.dumps(validator.run_benchmark_financial_audit(), indent=2))
        return

    for line in sys.stdin:
        if not line.strip(): continue
        try:
            req = json.loads(line)
            method = req.get("method")
            params = req.get("params", {})
            rid = req.get("id")

            if method == "tools/list":
                res = {
                    "tools": [
                        {"name": "audit_balance_sheet", "description": "Verify Assets = Liabilities + Stockholders' Equity."},
                        {"name": "audit_income_statement", "description": "Audit Gross Profit and Operating Income calculations."},
                        {"name": "audit_cross_footing", "description": "Verify 2D matrix row and column cross-footing arithmetic."},
                        {"name": "run_benchmark_financial_audit", "description": "Run standard accounting validation benchmarks."}
                    ]
                }
            elif method == "tools/call":
                tname = params.get("name")
                args = params.get("arguments", {})
                if tname == "audit_balance_sheet":
                    out = validator.audit_balance_sheet(args.get("balance_sheet_dict", {}))
                elif tname == "audit_income_statement":
                    out = validator.audit_income_statement(args.get("income_stmt_dict", {}))
                elif tname == "audit_cross_footing":
                    out = validator.audit_cross_footing(args.get("matrix_rows", []))
                elif tname == "run_benchmark_financial_audit":
                    out = validator.run_benchmark_financial_audit()
                else:
                    out = {"error": f"Unknown tool {tname}"}
                res = {"content": [{"type": "text", "text": json.dumps(out)}]}
            else:
                res = {"error": "Unsupported method"}
            print(json.dumps({"jsonrpc": "2.0", "id": rid, "result": res}), flush=True)
        except Exception as e:
            print(json.dumps({"jsonrpc": "2.0", "error": {"code": -32603, "message": str(e)}}), flush=True)

if __name__ == "__main__":
    main()
