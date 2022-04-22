N = int(input())
A= list(map(int, input().split()))
Q = int(input())
Query = [list(map(int, input().split())) for _ in range(Q)]
 
dic = {}
for i,a in enumerate(A):
    if dic.get(a):
        dic[a].append(i+1)
    else:
        dic[a] = [i+1]
        
import bisect
for q in Query:
    if dic.get(q[2]):
        idx = dic[q[2]]
#         print(idx, q)
        left = bisect.bisect_left(idx,q[0])
        right = bisect.bisect_right(idx,q[1])
        print(right-left)
    else:
        print(0)