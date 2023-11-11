import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from modal import Stub, web_endpoint
import services.BracketsInterface as bi
import services.TaxCalculator as tc

stub = Stub("net_income_calculator")

def getBracket(str) -> tuple:
    if str == "belgium":
        return bi.getBelgiumBracket(), "EUR"
    elif str == "switzerland":
        return bi.getSwitzerlandBracket(), "CHF"
    else:
        raise Exception("Invalid country")
    
@stub.function()
@web_endpoint()
def getNetIncome(gross_income: float, country: str) -> str:
    try:
        bracket, currency = getBracket(country.lower())
        calc = tc.TaxCalculator(bracket)
        net_income = calc.calculate_net_income(gross_income)
    except:
        return str(sys.exc_info()[1])
    
    return str(net_income) + " " + currency