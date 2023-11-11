from abc import ABC, abstractmethod

class Bracket(ABC):
    @property
    @abstractmethod
    def __init__(self) -> None:
        self.brackets: list[tuple[float,float,float]] = []

    @abstractmethod
    def get_brackets(self) -> list[tuple[float,float,float]]:
        pass