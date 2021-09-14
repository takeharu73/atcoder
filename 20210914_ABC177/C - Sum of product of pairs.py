MOD = 1000000007
N = int(input())
A = list(map(int, input().split()))
 
res = 0
sum_A = sum(A)
for a in A:
    sum_A -= a
    res += a*(sum_A%MOD)
    res = res%MOD
 
print(int(res))