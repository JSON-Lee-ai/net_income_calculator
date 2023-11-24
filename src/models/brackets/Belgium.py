import sys, os

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../")
from brackets.BracketABC import Bracket
from enums.Currency import Currency

class BelgiumTaxBrackets(Bracket):
    
    def __init__(self):
        super().__init__()
        self.brackets = [
            (0., 13870., 0.25),
            (13870., 24480., 0.40),
            (24480., 42370., 0.45),
            (42370., float('inf'), 0.50)
        ]
        self.currency = Currency.EUR

    def get_brackets(self):
        return self.brackets
    
    def get_currency(self):
        return self.currency.value
