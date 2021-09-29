def gcd(m, n):
    while m % n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm % oldn
    return n


class Fraction:
    def __init__(self, num, denum):
        self.numerator = num
        self.denumerator = denum

    def __str__(self):
        return str(self.numerator) + '/' + str(self.denumerator)

    def __add__(self, other):
        result_numerator = (self.numerator * other.denumerator) + \
            (other.numerator * self.denumerator)
        result_denumrator = self.denumerator * other.denumerator

        common_divisor = gcd(result_numerator, result_denumrator)

        return Fraction(result_numerator//common_divisor, result_denumrator//common_divisor)

    def __eq__(self, other):
        first_number = self.numerator * other.denumerator
        second_number = other.numerator * self.denumerator

        return first_number == second_number

    def __mul__(self, other):
        result_numerator = self.numerator * other.numerator
        result_denumerator = self.denumerator * other.denumerator

        common_divisor = gcd(result_numerator, result_numerator)

        return Fraction(result_numerator, result_denumerator)

    def __truediv__(self, other):
        result_numerator = self.numerator * other.denumerator
        result_denumerator = self.denumerator * other.numerator

        common_divisor = gcd(result_numerator, result_numerator)

        return Fraction(result_numerator, result_denumerator)

    def __sub__(self, other):
        result_numerator = (self.numerator * other.denumerator) - \
            (other.numerator * self.denumerator)
        result_denumrator = self.denumerator * other.denumerator

        common_divisor = gcd(result_numerator, result_denumrator)

        return Fraction(result_numerator//common_divisor, result_denumrator//common_divisor)

    def __gt__(self, other):
        first_number = self.numerator * other.denumerator
        second_number = other.numerator * self.denumerator

        return first_number > second_number

    def __ge__(self, other):
        first_number = self.numerator * other.denumerator
        second_number = other.numerator * self.denumerator

        return first_number >= second_number
