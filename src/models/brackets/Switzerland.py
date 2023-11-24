import sys, os

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../")
from brackets.BracketABC import Bracket
from enums.Currency import Currency

class SwitzerlandTaxBrackets(Bracket):
    def __init__(self) -> None:
        super().__init__()
        self.brackets: list[tuple[float,float,float]] = [
            (0., 14800., 0.),
            (14800., 32200., 0.0077),
            (32200., 42200., 0.0088),
            (42200., 56200., 0.0264),
            (56200., 73900., 0.0297),
            (73900., 79600., 0.0594),
            (79600., 105500.,  0.066),
            (105500., 137200., 0.088),
            (137200., 179400., 0.11),
            (179400., 769600., 0.132),
            (769600., float('inf'), 0.115)
        ]
        self.currency = Currency.CHF

    def get_brackets(self):
        return self.brackets
    
    def get_currency(self):
        return self.currency.value
    