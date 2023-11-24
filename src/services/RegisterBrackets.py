import sys, os

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../")
from services.BracketFactory import BracketFactory
from models.brackets import Belgium, Switzerland, France

def register_brackets():
    BracketFactory.register("belgium", Belgium.BelgiumTaxBrackets)
    BracketFactory.register("switzerland", Switzerland.SwitzerlandTaxBrackets)
    BracketFactory.register("france", France.FranceTaxBrackets)

register_brackets()