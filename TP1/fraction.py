class Fraction:
    def __init__(self, numerator: int, denominator: int):
        self.numerator = numerator
        self.denominator = denominator

    def display(self):
        print(f"{self.numerator}/{self.denominator}")

    def add(self, fraction: Fraction) -> Fraction:
        return Fraction(
            self.numerator * fraction.denominator
            + fraction.numerator * self.denominator,
            self.denominator * fraction.denominator,
        )

    def subtract(self, fraction: Fraction) -> Fraction:
        return Fraction(
            self.numerator * fraction.denominator
            - fraction.numerator * self.denominator,
            self.denominator * fraction.denominator,
        )

    def multiply(self, fraction: Fraction) -> Fraction:
        return Fraction(
            self.numerator * fraction.numerator,
            self.denominator * fraction.denominator,
        )

    def divide(self, fraction: Fraction) -> Fraction:
        return Fraction(
            self.numerator * fraction.denominator,
            self.denominator * fraction.numerator,
        )

if __name__ == "__main__":
    f1 = Fraction(1, 2)
    f2 = Fraction(6, 5)
    f3 = f1.add(f2)
    f4 = f1.subtract(f2)
    f5 = f1.multiply(f2)
    f6 = f1.divide(f2)

    f1.display()
    f2.display()
    f3.display()
    f4.display()
    f5.display()
    f6.display()
