from math import gcd

class Fraction :

    def __init__ (self, numerator, denominator) :
        if denominator == 0:
            raise ValueError ('Denominator can be zero')
        if type(numerator) != int:
            raise TypeError ('Numerator must be an integer')
        if type(denominator) != int:
            raise TypeError ('Denominator can be zero')
        
        common_divisor = gcd (numerator, denominator)
        self.numerator = numerator // common_divisor
        self.denominator = denominator // common_divisor

    def print(self):
        print(f'{self.numerator}/{self.denominator}')

    def __add__ (self, other):
        if type(other) != Fraction:
            raise TypeError ('Must insert "Fraction"')
        
        den = self.denominator*other.denominator
        num = self.numerator*other.denominator + other.numerator*self.denominator
        return Fraction (num, den)
    
    def __sub__ (self, other):
        if type(other) != Fraction:
            raise TypeError ('Must insert "Fraction"')
        
        den = self.denominator*other.denominator
        num = self.numerator*other.denominator - other.numerator*self.denominator
        return Fraction (num, den)
    
    def __mul__ (self, other):
        if type(other) != Fraction:
            raise TypeError ('Must insert "Fraction"')
        
        den = self.denominator*other.denominator
        num = self.numerator*other.numerator
        return Fraction (num, den)
    
    def __truediv__ (self, other):
        if type(other) != Fraction:
            raise TypeError ('Must insert "Fraction"')
        
        den = self.denominator*other.numerator
        num = self.numerator*other.denominator
        return Fraction (num, den)
    
    def turnintofloat (self):
        return float(self.numerator / self.denominator)
    
frac1 = Fraction (1, 2)
frac2 = Fraction (3, 4)

(frac1 + frac2).print()
(frac1 - frac2).print()
(frac1 * frac2).print()
(frac1 / frac2).print()
print(frac1.turnintofloat())