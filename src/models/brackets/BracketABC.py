from abc import ABC, abstractmethod
from typing import List, Tuple

class Bracket(ABC):
    def __init__(self) -> None:
        self.brackets: List[Tuple[float,float,float]] = []

    @abstractmethod
    def get_brackets(self) -> List[Tuple[float,float,float]]:
        pass