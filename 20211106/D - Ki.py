from collections import deque
import copy

# データ数の多いテストケースで、"RecursionError: maximum recursion depth exceeded"が発生してしまう。デフォルトでは3000回以上再帰処理を行うとこのエラーが発生するみたい。今回max200000なので変更が必要。
import sys
sys.setrecursionlimit(10**9)
 
N,Q = list(map(int, input().split()))
A,B = [], []
AB = [list(map(int, input().split())) for _ in range(N-1)]
PX = [list(map(int, input().split())) for _ in range(Q)]
 
graph = [deque() for _ in range(N+1)]

# 無向グラフ
for a,b in AB:
    graph[a].append(b)
    graph[b].append(a)
    
visited = [0]*(N+1)
score = [0]*(N+1)
    
for p,x in PX:
    score[p] += x

# 累積和を使うことで、全ての根以下の枝葉に根の値を加算することを実現する。
def dfs(i, s):
    if not visited[i]:
        score[i] += s
        visited[i] = 1
    
        for next_i in graph[i]:
            dfs(next_i, score[i])
 
dfs(1,0)
 
print(" ".join([str(s) for s in score[1:]]))
