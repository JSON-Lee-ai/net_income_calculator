class TaxCalculator:
    def __init__(self, tax_brackets: list[tuple[float, float, float]]) -> None:
        self.tax_brackets = tax_brackets

    def calculate_net_income(self, gross_income: float) -> float:
        total_tax = 0.0
        remaining_income = gross_income

        for bracket in self.tax_brackets:
            bracket_min, bracket_max, tax_rate = bracket
            if remaining_income <= 0:
                break

            income_in_bracket = min(bracket_max - bracket_min, remaining_income)
            tax_in_bracket = income_in_bracket * tax_rate
            total_tax += tax_in_bracket
            remaining_income -= income_in_bracket

        net_income = gross_income - total_tax
        return net_income
