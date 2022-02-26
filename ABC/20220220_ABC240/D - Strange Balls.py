from collections import deque
N = list(map(int, input().split()))
A = list(map(int, input().split()))
 
res = 0
continuous = deque([])
lastball = deque([])
for i, a in enumerate(A):
    if not lastball:
        lastball.append(a)
        continuous.append(1)
#         print(continuous[-1], lastball[-1])
        res += 1
        print(res)
        continue
    if a == lastball[-1]:
        continuous[-1] += 1
    else:
        lastball.append(a)
        continuous.append(1)
#     print(continuous[-1], lastball[-1])
    if continuous[-1] == lastball[-1]:
        continued_num = continuous.pop()
        lastball.pop()
        res -= continued_num - 1
    else:
        res += 1
    print(res)