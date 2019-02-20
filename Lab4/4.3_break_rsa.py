from fractions import Fraction
from decimal import *
import math
import sys
sys.setrecursionlimit(1500)

class BreakRSA():
    def __init__(self,cipher,e,n):
        self.cipher=cipher
        self.e=e
        self.n=n
        self.d=1
        self.fractional_parts=[]
        self.plain_text=0

    def getContinuedFractionSum(self,li):
        a = Fraction(0)
        for i in li:
            b = Fraction(1, 1)
            a = b._div(a._add(i))
        return a

    def bigmod(self,m, e, n):
        if e == 0:
            return 1
        elif e == 1:
            return m
        elif m == 0 or n == 1:
            return 0
        ans = self.bigmod(m, (e // 2), n) % n
        ans = (ans * ans) % n
        if e % 2 == 1:
            ans = (ans * m) % n
        return ans

    def validation_check(self,fractional_parts):
        rev_fractional_part = list(reversed(fractional_parts))
        rational_approximation = self.getContinuedFractionSum(rev_fractional_part)
        self.d = rational_approximation.denominator
        k = rational_approximation.numerator
        if self.d % 2 == 0 or (self.e * self.d - 1) % k != 0:
            return False
        phi = (self.e * self.d - 1) / k
        b = -(self.n - phi + 1)
        determinant = b * b - 4 * self.n

        if determinant < 0:
            return False
        if ((-b + math.sqrt(Decimal(determinant))) / 2) % 1 != 0 or (
                (-b - math.sqrt(Decimal(determinant))) / 2) % 1 != 0:
            return False
        self.plain_text=self.bigmod(self.cipher, self.d, self.n)
        return True

    def ecFraction(self,n, e):
        if e == 0:
            return n
        self.fractional_parts.append(n // e)
        if self.validation_check(self.fractional_parts) == True:
            return
        self.ecFraction(e, n % e)


def main():
    cipher = open("4.3_ciphertext.hex", "r").read()
    e = open("4.4_public_key.hex", "r").read()
    n = open("4.5_modulo.hex", "r").read()
    print 'Public key :',e
    cipher = int(cipher, 16)
    e = int(e, 16)
    n = int(n, 16)

    rsa_breaker=BreakRSA(cipher,e,n)
    rsa_breaker.ecFraction(n, e)

    print 'Private key : ',hex(rsa_breaker.d)[2:]
    print 'Plain Text : ',hex(rsa_breaker.plain_text)[2:]


if __name__== "__main__":
    main()

