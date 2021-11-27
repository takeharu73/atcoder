N,W = list(map(int, input().split()))
AB = {}
cnt = 0
for i in range(N):
    a,b = list(map(int, input().split()))
    if AB.get(a) is None:
        AB[a] = b
    else:
        AB[a] += b
        cnt += 1

AB = sorted(AB.items(), key=lambda x:x[0], reverse=True)

res = 0
weight = 0
for i in range(N-cnt):
    if AB[i][1] >= W-weight:
        res += AB[i][0]*(W-weight)
        break
    else:
        res += AB[i][0]*AB[i][1]
        weight += AB[i][1]
print(res)