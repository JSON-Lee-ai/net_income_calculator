import sys, os

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../")
from brackets.BracketABC import Bracket
from enums.Currency import Currency

class FranceTaxBrackets(Bracket):
    
    def __init__(self):
        super().__init__()
        self.brackets = [
            (0.0, 10777.0, 0.0),
            (10778.0, 27478.0, 0.11),
            (27479.0, 78570.0, 0.30),
            (78571.0, 168994.0, 0.41),
            (168995.0, float('inf'), 0.45)
        ]
        self.currency = Currency.EUR

    def get_brackets(self):
        return self.brackets
    
    def get_currency(self):
        return self.currency.value
