N, M = list(map(int, input().split()))
A = []
for i in range(N):
    A.append(list(map(int, input().split())))

max_p = 0
for i in range(M-1):
    for j in range(i+1,M):
        p = 0
        for k in range(N):
            p += max(A[k][i], A[k][j])
        if max_p < p:
            max_p = p
        p = 0
print(max_p)