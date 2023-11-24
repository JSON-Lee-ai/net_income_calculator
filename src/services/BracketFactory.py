import sys, os

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../")

class BracketFactory:
    registry = {}

    @classmethod
    def register(cls, country: str, bracket_class):
        cls.registry[country] = bracket_class

    @classmethod
    def get_bracket(cls, country: str):
        bracket_class = cls.registry.get(country)
        if bracket_class:
            return bracket_class()
        else:
            raise ValueError(f"No bracket found for country: {country}")
