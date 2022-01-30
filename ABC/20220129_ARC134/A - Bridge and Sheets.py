N, L, W = list(map(int,input().split()))
A = list(map(int,input().split()))

remain = []
prev = 0
for a in A:
    if a-prev >0:
        remain.append(a-prev)
    prev = a + W
remain.append(L-prev)

res = 0
for r in remain:
    if r%W == 0:
        res += r//W
    else:
        res += r//W+1

print(res)