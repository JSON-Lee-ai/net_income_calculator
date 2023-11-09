class BelgiumTaxBrackets:
    def __init__(self) -> None:
        self.brackets: list[tuple[float,float,float]] = [
            (0., 13870., 0.25),
            (13870., 24480., 0.40),
            (24480., 42370., 0.45),
            (42370., float('inf'), 0.50)
        ]