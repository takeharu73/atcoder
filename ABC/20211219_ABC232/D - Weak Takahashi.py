# 薄氷渡りを参考に実装→TLE
# →visited[i] = 0の処理が不要だった(今回は右か下かにしか行かないので、visitedをリセットする必要がない)
# visited[i] = 0をコメントアウトするとAC

from collections import deque
import sys
import copy
sys.setrecursionlimit(10**9)
 
N,M = list(map(int, input().split()))
A = []
for n in range(N):
    A.extend(list(input()))
 
wait = [[] for _ in range(M*N)]
for n in range(N):
    for m in range(M):
        if A[n*M+m]==".":
            if n!=N-1:
                if A[(n+1)*M+m]==".":
                    wait[n*M+m].append((n+1)*M+m)
            if m!=M-1:
                if A[n*M+m+1]==".":
                    wait[n*M+m].append(n*M+m+1)
res = [0]*(M*N)
 
def dfs(first_i, i):
    global cnt
    if not visited[i]:
        visited[i] = 1
        cnt+=1
        if res[first_i]<cnt:
            res[first_i]=cnt
 
        for next_cell in wait[i]:
            dfs(first_i, next_cell)
        else:
            cnt -= 1
            # visited[i] = 0
 
f = 0
visited = [0]*(M*N)
cnt = 0
dfs(f, f)
        
print(max(res))