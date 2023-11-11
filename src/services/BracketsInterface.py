import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../")

from models.brackets import Belgium, Switzerland

def getBelgiumBracket() -> list[tuple[float, float, float]]:
    return Belgium.BelgiumTaxBrackets().get_brackets()

def getSwitzerlandBracket() -> list[tuple[float, float, float]]:
    return Switzerland.SwitzerlandTaxBrackets().get_brackets()
