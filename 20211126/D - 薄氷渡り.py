from collections import deque
import sys
import copy
sys.setrecursionlimit(10**9)
 
M = int(input())
N = int(input())
A = []
for n in range(N):
    A.extend(list(map(int, input().split())))
 
# wait = [deque() for _ in range(M*N)]
wait = [[] for _ in range(M*N)]
for n in range(N):
    for m in range(M):
        if A[n*M+m]==1:
            if n!=N-1:
                if A[(n+1)*M+m]==1:
                    wait[n*M+m].append((n+1)*M+m)
            if m!=M-1:
                if A[n*M+m+1]==1:
                    wait[n*M+m].append(n*M+m+1)
            if m!=0:
                if A[n*M+m-1]==1:
                    wait[n*M+m].append(n*M+m-1)
            if n!=0:
                if A[(n-1)*M+m]==1:
                    wait[n*M+m].append((n-1)*M+m)
wait_ori = copy.deepcopy(wait)
res = [0]*(M*N)
 
def dfs(first_i, i):
    global cnt
    if not visited[i]:
        visited[i] = 1
        cnt+=1
        if res[first_i]<cnt:
            res[first_i]=cnt
 
        # pop()してしまうと、先に訪問したセルがwaitから削除されてしまう。
        # それを防ぐため、forループとする。
        # while wait[i]:
        #     next_cell = wait[i].pop()
        for next_cell in wait[i]:
            dfs(first_i, next_cell)
        else:
            cnt -= 1
            visited[i] = 0
 
for f in range(M*N):
    if A[f]==1:
        wait = copy.deepcopy(wait_ori)
        visited = [0]*(M*N)
        cnt = 0
        dfs(f, f)
        
print(max(res))