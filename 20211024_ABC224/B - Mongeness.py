H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
 
flg = 0
for i in range(H):
    for j in range(W):
        for k in range(i+1,H):
            for m in range(j+1,W):
                if A[i][j]+A[k][m]>A[i][m]+A[k][j]:
                    flg = 1
if flg == 0:
    print("Yes")
else:
    print("No")