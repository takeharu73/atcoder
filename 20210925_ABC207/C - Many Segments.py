N = int(input())
 
T = [list(map(int, input().split(" "))) for _ in range(N)]
 
L = []
for i,t in enumerate(T):
    L.append([0,0])
    if t[0]==1:
        L[i][0]=t[1]
        L[i][1]=t[2]
    elif t[0]==2:
        L[i][0]=t[1]
        L[i][1]=t[2]-0.1
    elif t[0]==3:
        L[i][0]=t[1]+0.1
        L[i][1]=t[2]
    else:
        L[i][0]=t[1]+0.1
        L[i][1]=t[2]-0.1
 
res = 0
for i in range(N):
    for j in range(i+1, N):
        if not (L[i][1]<L[j][0] or L[i][0]>L[j][1]):
            res += 1
 
print(res)