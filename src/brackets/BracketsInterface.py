import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from countries import Belgium, Switzerland

def getBelgiumBracket() -> list[tuple[float, float, float]]:
    return Belgium.BelgiumTaxBrackets().brackets

def getSwitzerlandBracket() -> list[tuple[float, float, float]]:
    return Switzerland.SwitzerlandTaxBrackets().brackets
