import sys, json
from client import FinancialFormulaAuditValidator

def main():
    print("Testing FinancialFormulaAuditValidator...")
    validator = FinancialFormulaAuditValidator()
    res = validator.run_benchmark_financial_audit()
    print(json.dumps(res, indent=2))
    assert res["benchmark_status"] == "PASSED"
    assert res["balance_sheet_status"] == "BALANCED"
    assert res["cross_footing_status"] == "PERFECT_MATCH"
    print("All Financial Formula Audit Validator tests passed successfully!")

if __name__ == "__main__":
    main()
