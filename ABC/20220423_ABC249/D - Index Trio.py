N= int(input())
A = list(map(int, input().split()))
 
import collections
count_A = collections.Counter(A)
# 各数の約数を求め、forループ→約数と割った後の数がそれぞれ存在する数をかけて、resに追加
 
def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]
 
res = 0
for a in count_A.keys():
    for d in make_divisors(a):
        if count_A.get(d):
            if count_A.get(int(a/d)):
                res += count_A[a]*count_A[d]*count_A[int(a/d)]
 
print(res)