import unittest
from inspect import getmembers, isfunction
from unittest.mock import Mock
import sys, os

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../")

from services.BracketFactory import BracketFactory
from models.brackets import Belgium, Switzerland

class TestBracketFactory(unittest.TestCase):
    def setUp(self):
        # Clear the registry before each test
        BracketFactory.registry = {}

    def test_register(self):
        # Arrange
        country = "test_country"
        bracket_class = Mock()

        # Act
        BracketFactory.register(country, bracket_class)

        # Assert
        self.assertEqual(BracketFactory.registry[country], bracket_class)

    def test_get_bracket_with_registered_country(self):
        # Arrange
        country = "test_country"
        bracket_class = Mock()
        BracketFactory.register(country, bracket_class)

        # Act
        result = BracketFactory.get_bracket(country)

        # Assert
        self.assertEqual(result, bracket_class.return_value)
        bracket_class.assert_called_once()

    def test_get_bracket_with_unregistered_country(self):
        # Arrange
        country = "unregistered_country"

        # Act & Assert
        with self.assertRaises(ValueError) as context:
            BracketFactory.get_bracket(country)

        self.assertEqual(str(context.exception), f"No bracket found for country: {country}")

    def test_get_bracket_returns_correct_values_for_belgium(self):
        # Arrange
        country = "belgium"
        BracketFactory.register(country, Belgium.BelgiumTaxBrackets)

        # Act
        bracket = BracketFactory.get_bracket(country)

        # Assert
        self.assertIsInstance(bracket, Belgium.BelgiumTaxBrackets)

    def test_get_bracket_returns_correct_values_for_switzerland(self):
        # Arrange
        country = "switzerland"
        BracketFactory.register(country, Switzerland.SwitzerlandTaxBrackets)

        # Act
        bracket = BracketFactory.get_bracket(country)

        # Assert
        self.assertIsInstance(bracket, Switzerland.SwitzerlandTaxBrackets)

if __name__ == '__main__':
    unittest.main()