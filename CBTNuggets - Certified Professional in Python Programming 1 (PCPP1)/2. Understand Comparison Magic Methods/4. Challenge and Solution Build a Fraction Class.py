class Fraction:
    def __init__(self, top, bottom):
        self.top = top
        self.bottom = bottom

    def __eq__(self, other):
        if isinstance(other, Fraction):

            return self.top / self.bottom == other.top / other.bottom
        elif isinstance(other, int) or isinstance(other, float):
            return self.top / self.bottom == other
        else:
            NotImplemented

    def __gt__(self, other):
        return self.top / self.bottom > other.top / other.bottom


f1 = Fraction(2, 5)
f2 = Fraction(2, 5)
f3 = Fraction(3, 22)
f4 = Fraction(6, 44)
print(f1 > f2)
print(f1 > f2)
print(f1 < f2)
print(f3 == f4)
