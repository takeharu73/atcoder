# DFSには気付くも、難しく考えすぎてしまい、提出できず。

N = int(input())
A = [list(map(int, input().split())) for _ in range(2*N-1)]

B = [[0]*2*N for _ in range(2*N)]
for n in range(2*N-1):
    for m in range(2*N-n-1):
        B[n][n+m+1]=A[n][m]
for n in range(2*N-1):
    for m in range(2*N-n-1):
        B[n+m+1][n]=A[n][m]

remain = [i for i in range(2*N)]

import itertools


def dfs(new_c, remain, res, final_res):
    print(remain, new_c)
    res += B[new_c[0]][new_c[1]]
    remain.remove(new_c[0])
    remain.remove(new_c[1])
    comb = itertools.combinations(remain, 2)
    if remain:
        for c in comb:
            res, remain, comb, final_res = dfs(c, remain, res, final_res)
    else:
        return res, remain, comb, final_res
    if final_res < res:
        final_res = res
    return res, remain, comb, final_res

final_res = 0
res = 0
comb = list(itertools.combinations(remain, 2))
for c in comb:
    res, remain, comb, final_res = dfs(c, remain, res, final_res)

    
print(final_res)




##### 以下は他の方の回答から。
N = int(input())
N *= 2
A = []
for i in range(N-1):
    A.append([0]*(i+1)+[int(x) for x in input().split()])
 
ans = 0
used = [0]*N
 
def dfs(n, xor):
    global ans
    if n == N:
        ans = max(ans, xor)
        return
 
    for i in range(N):
        if not used[i]:
            used[i] = 1
            break
    for j in range(i+1, N):
        if not used[j]:
            used[j] = 1
            dfs(n+2, xor^A[i][j])
            used[j] = 0
    used[i] = 0
 
dfs(0,0)
print(ans)