### 尺取り法には気づけたが、間にXより大きい数／Yより小さい数が入るケースについて考慮できておらず、WA


N,X,Y = list(map(int, list(input().split())))
A = list(map(int, list(input().split())))

# print(A)

from collections import deque
max_idx = deque()
min_idx = deque()

for i in range(N):
    if A[i] == X:
        max_idx.append(i)
    elif A[i] == Y:
        min_idx.append(i)

if len(min_idx) == 0 or len(max_idx) == 0:
    print(0)
    exit()
left = max(max_idx[0], min_idx[0])
right = max(max_idx[-1], min_idx[-1])

# print(left, right)
# print(right-left+1)

res = right-left+1
# res = 0
# print(max_idx)
# print(min_idx)
# print(Y)

for i in range(N):
#     print(i,A[i],res,left,right)
    if A[i] == X:
        max_idx.popleft()
        if len(max_idx)==0:
            break
        if max_idx[0] > left:
            left = max_idx[0]
    if A[i] == Y:
        min_idx.popleft()
        if len(min_idx)==0:
            break
        if min_idx[0] > left:
            left = min_idx[0]
    res += (right-left+1)
            
print(res)