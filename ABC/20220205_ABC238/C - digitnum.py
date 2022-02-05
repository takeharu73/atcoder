from decimal import Decimal
from fractions import Fraction

N = int(input())

mod = Decimal(str(998244353))
len_N = len(str(N))

res = 0
for l in range(len_N-1):
    last = 10**(l+1)-10**l
    last = Fraction(str(last))
    res += int(Fraction(str((1+last)*last))/Fraction('2'))

last = N-10**(len_N-1)+1
last = Fraction(str(last))
res += int(Fraction(str((1+last)*last))/Fraction('2'))

print(res%mod)