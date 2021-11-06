from collections import deque
import copy
 
import sys
sys.setrecursionlimit(10**9)
 
N,Q = list(map(int, input().split()))
A,B = [], []
AB = [list(map(int, input().split())) for _ in range(N-1)]
PX = [list(map(int, input().split())) for _ in range(Q)]
 
graph = [deque() for _ in range(N+1)]
for a,b in AB:
    graph[a].append(b)
    graph[b].append(a)
    
visited = [0]*(N+1)
score = [0]*(N+1)
    
for p,x in PX:
    score[p] += x
    
def dfs(i, s):
    if not visited[i]:
        score[i] += s
        visited[i] = 1
    
        for next_i in graph[i]:
            dfs(next_i, score[i])
 
dfs(1,0)
 
print(" ".join([str(s) for s in score[1:]]))