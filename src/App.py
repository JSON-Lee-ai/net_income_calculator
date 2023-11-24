import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../")

class App:
    def __init__(self, bracket_factory, tax_calculator_cls):
        self.bracket_factory = bracket_factory
        self.tax_calculator_cls = tax_calculator_cls

    def getNetIncome(self, gross_income: float, country: str) -> str:
        try:
            bracketClass = self.bracket_factory.get_bracket(country)
            
            bracket = bracketClass.get_brackets()
            currency = bracketClass.get_currency()

            calculator = self.tax_calculator_cls(bracket)
            net_income = calculator.calculate_net_income(gross_income)
        except:
            return str(sys.exc_info()[1])
        
        return str(net_income) + " " + currency
    
def main():
    import services.BracketFactory as bf
    import services.TaxCalculator as tc

    bracket_factory = bf.BracketFactory()
    tax_calculator_cls = tc.TaxCalculator

    app = App(bracket_factory, tax_calculator_cls)
    print(app.getNetIncome(100000, "switzerland"))

if __name__ == "__main__":
    main()