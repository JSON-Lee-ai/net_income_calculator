import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import services.BracketsInterface as bi
import services.TaxCalculator as tc

class App:
    def __init__(self):
        pass

    def getBracket(self, str) -> tuple:
        if str == "belgium":
            return bi.getBelgiumBracket(), "EUR"
        elif str == "switzerland":
            return bi.getSwitzerlandBracket(), "CHF"
        else:
            raise Exception("Invalid country")
        

    def getNetIncome(self, gross_income: float, country: str) -> str:
        try:
            bracket, currency = self.getBracket(country.lower())
            calc = tc.TaxCalculator(bracket)
            net_income = calc.calculate_net_income(gross_income)
        except:
            return str(sys.exc_info()[1])
        
        return str(net_income) + " " + currency