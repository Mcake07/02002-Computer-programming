class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator, self.denominator = numerator, denominator
    def __str__(self):
        return f'{self.numerator}/{self.denominator}'
    def simplify(self):
        num_biggie = False
        denom_biggie = False
        smallest = None
        new_num = None
        new_denom = None
        if self.numerator > self.denominator: num_biggie = True
        elif self.numerator < self.denominator: num_biggie = True
        if not (num_biggie and denom_biggie): self.numerator, self.denominator = 1,1
        elif num_biggie: smallest = self.denominator
        else: smallest = self.numerator
        for i in range(smallest):
            if self.numerator / i == 0.0 and self.denominator / i == 0.0: 
                self.numerator = int(self.numerator / i)
                self.denominator = int(self.denominator / i)
                break
    def __eq__(self, other):
        left = self.numerator * self.denominator
        right = other.numerator * other.denominator
        return left == right