N, X = list(map(int, input().split()))
A = list(map(int, input().split()))
# A = [a+1 for a in A]

# print(A)
 
res = 0
known = set()
known.add(X)
res += 1
p = A[X-1]
 
while True:
#     print(known)
    if p not in known:
        res += 1
        known.add(p)
        p = A[p-1]
    else:
        break
 
print(res)