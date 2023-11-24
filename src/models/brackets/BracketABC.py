from abc import ABC, abstractmethod
from typing import List, Tuple
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../")

from enums.Currency import Currency

class Bracket(ABC):
    def __init__(self) -> None:
        self.brackets: List[Tuple[float,float,float]] = []
        self.currency: Currency.DEFAULT

    @abstractmethod
    def get_brackets(self) -> List[Tuple[float,float,float]]:
        pass

    @abstractmethod
    def get_currency(self) -> str:
        return self.currency.value