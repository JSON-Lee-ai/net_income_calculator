import unittest
from inspect import getmembers, isfunction
import sys, os

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../")

from src.models import BracketsInterface as bi

class TestTaxBrackets(unittest.TestCase):
    def test_all_brackets(self):
        for name, func in getmembers(bi, isfunction):
            if name.startswith('get') and 'Bracket' in name:
                brackets = func()
                self.assertIsNotNone(brackets)  # assuming brackets should not be None
                self.assertIsInstance(brackets, list)  # check if brackets is a list
                for bracket in brackets:
                    self.assertIsInstance(bracket, tuple)  # check if each item in the list is a tuple
                    self.assertEqual(len(bracket), 3)  # check if each tuple has 3 items
                    for item in bracket:
                        self.assertIsInstance(item, float)  # check if each item in the tuple is a float

if __name__ == '__main__':
    unittest.main()