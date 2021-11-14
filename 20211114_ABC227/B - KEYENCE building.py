import collections

N = int(input())
S = list(map(int, input().split()))
S_c = collections.Counter(S)
# print(S_c)

for a in range(1,150):
    for b in range(a, 150):
        m = 4*a*b+3*a+3*b
        if m in S_c:
            S_c[m] = 0
        if m>1000:
            break
# print(S_c)
res = sum(S_c.values())
print(res)