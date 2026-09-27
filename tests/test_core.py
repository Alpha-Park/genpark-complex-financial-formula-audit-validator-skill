import unittest
from genpark_financial_audit import FinancialFormulaAuditValidator as Client

class CoreTests(unittest.TestCase):

    def test_missing_cannot_pass(self):
        with self.assertRaises(ValueError): Client().audit_balance_sheet({})
        with self.assertRaises(ValueError): Client().audit_income_statement({})
    def test_reported_total_cannot_hide_mismatch(self):
        out = Client().audit_balance_sheet(dict(total_assets=100,total_liabilities=10,stockholders_equity=20,total_liabilities_and_equity=100))
        self.assertFalse(out["is_balanced"])
    def test_zero_component(self):
        out = Client().audit_balance_sheet(dict(total_assets=100,total_liabilities=40,stockholders_equity=60,current_assets=0,non_current_assets=90))
        self.assertFalse(out["is_balanced"])
    def test_grand_total(self):
        self.assertEqual(Client().audit_cross_footing([[1,2,3],[1,2,999]])["status"], "DISCREPANCY_DETECTED")
        self.assertEqual(Client().audit_cross_footing([[1,2,3],[1,2,3]])["status"], "PERFECT_MATCH")
    def test_net_income(self):
        out = Client().audit_income_statement(dict(revenue=100,cogs=20,gross_profit=80,operating_expenses=10,operating_income=70,tax_expense=10,net_income=99))
        self.assertEqual(out["status"], "DISCREPANCY_DETECTED")
    def test_nonfinite_and_ragged(self):
        with self.assertRaises(ValueError): Client().audit_cross_footing([[1,2],[3]])
        with self.assertRaises(ValueError): Client().audit_balance_sheet(dict(total_assets=float('nan'),total_liabilities=0,stockholders_equity=0))

if __name__ == "__main__": unittest.main()
