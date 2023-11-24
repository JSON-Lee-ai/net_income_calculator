import unittest
from unittest.mock import Mock, patch
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../")
from App import App

class TestApp(unittest.TestCase):
    def setUp(self):
        self.bracket_factory = Mock()
        self.tax_calculator_cls = Mock()
        self.app = App(self.bracket_factory, self.tax_calculator_cls)

    def test_getNetIncome(self):
        # Arrange
        gross_income = 100000
        country = "switzerland"
        bracket = [(0.0, 20000.0, 0.0), (20000.0, 40000.0, 0.1), (40000.0, 100000.0, 0.2), (100000.0, float('inf'), 0.3)]
        currency = "CHF"
        net_income = 80000

        bracket_class_mock = Mock()
        bracket_class_mock.get_brackets.return_value = bracket
        bracket_class_mock.get_currency.return_value = currency
        self.bracket_factory.get_bracket.return_value = bracket_class_mock

        tax_calculator_mock = Mock()
        tax_calculator_mock.calculate_net_income.return_value = net_income
        self.tax_calculator_cls.return_value = tax_calculator_mock

        # Act
        result = self.app.getNetIncome(gross_income, country)

        # Assert
        self.assertEqual(result, str(net_income) + " " + currency)
        self.bracket_factory.get_bracket.assert_called_once_with(country)
        bracket_class_mock.get_brackets.assert_called_once()
        bracket_class_mock.get_currency.assert_called_once()
        self.tax_calculator_cls.assert_called_once_with(bracket)
        tax_calculator_mock.calculate_net_income.assert_called_once_with(gross_income)

if __name__ == '__main__':
    unittest.main()