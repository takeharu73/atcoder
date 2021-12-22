import sys
sys.setrecursionlimit(10**7)
 
N = int(input())
T, K, A = [],[],[]
for i in range(N):
    t, k, *a = list(map(int, input().split()))
    T.append(t)
    K.append(k)
    A.append(a)
    
N -= 1
A = [[aa-1 for aa in a] for a in A]
 
need = set()
need.add(N)
 
def dfs(a):
    if a not in need:
        need.add(a)
    while True:
        if A[a]:
            b = A[a].pop()
            dfs(b)
        else:
            break
        
for a in A[N]:
    dfs(a)
    
res = 0
for n in need:
    res += T[n]
    
print(res)