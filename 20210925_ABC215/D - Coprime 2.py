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
 
N, M=list(map(int, input().split()))
A = list(map(int,input().split()))
A_cmb = set()
for a in A:
    C = make_divisors(a)
    for c in C:
        A_cmb.add(c)
 
if 1 in A_cmb:
    A_cmb.remove(1)
 
# gcd
B = set([i for i in range(1,M+1)])
 
for a in A_cmb:
    for i in range(1, M//a+1):
        if a*i in B:
            B.remove(a*i)
 
print(len(B))            
for b in B:
    print(b)