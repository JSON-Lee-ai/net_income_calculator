import unittest
import sys, os

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../")

from src.App import App
class TestApp(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.app = App()

    def test_getBracket_belgium(self):
        bracket, currency = self.app.getBracket("belgium")
        self.assertIsNotNone(bracket)
        self.assertEqual(currency, "EUR")

    def test_getBracket_switzerland(self):
        bracket, currency = self.app.getBracket("switzerland")
        self.assertIsNotNone(bracket)
        self.assertEqual(currency, "CHF")

    def test_getBracket_invalid_country(self):
        with self.assertRaises(Exception):
            self.app.getBracket("invalid_country")

    def test_getNetIncome_belgium(self):
        net_income = self.app.getNetIncome(100000, "belgium")
        self.assertIsNotNone(net_income)
        self.assertTrue(net_income.endswith("EUR"))

    def test_getNetIncome_switzerland(self):
        net_income = self.app.getNetIncome(100000, "switzerland")
        self.assertIsNotNone(net_income)
        self.assertTrue(net_income.endswith("CHF"))

if __name__ == '__main__':
    unittest.main()