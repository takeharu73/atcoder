N, M = list(map(int, input().split()))
K, S = [], []
 
for i in range(M):
    ks = list(map(int, input().split()))
    ki = ks[0]
    si = ks[1:]
    K.append(ki)
    S.append(si)
p = list(map(int, input().split()))
 
res = 0
for i in range(2**N):
    switch = []
    for j in range(N):
        if(i>>j)&1:
            switch.append(j)
    flg = 0
    for m in range(M):
        cnt = 0
        for s in S[m]:
            if s-1 in switch: 
                cnt += 1
        if cnt%2 != p[m]:
            flg = 1
            break
        
    if flg == 0:
        res += 1
 
print(res)