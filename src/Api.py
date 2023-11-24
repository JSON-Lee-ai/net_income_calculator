from modal import Stub, web_endpoint
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import services.BracketFactory as bf
import services.TaxCalculator as tc
from App import App
stub = Stub("net_income_calculator")

app = App(bf.BracketFactory(), tc.TaxCalculator)
@stub.function()
@web_endpoint()
def calculateNetIncome(gross_income: float, country: str) -> str:
    try:
        response = app.getNetIncome(gross_income, country)
    except:
        return str(sys.exc_info()[1])
    
    return response