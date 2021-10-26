dd = int(input())
n = int(input())
m = int(input())
D = [int(input()) for _ in range(n-1)]
K = [int(input()) for _ in range(m)]

D.append(0)
D.append(dd)
D = sorted(D)

import bisect

res = 0
for k in K:
    index = bisect.bisect_left(D, k)
    if D[index]-k>k-D[index-1]:
        res+=(k-D[index-1])
    else:
        res+=(D[index]-k)
    
print(res)