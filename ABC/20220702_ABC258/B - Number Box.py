##### 全探索ではTLEになると思い、途中でDFSに方針転換してしまい、時間切れ懸念のためスキップ
##### 普通に全探索すれば解けた。最初に制約条件をしっかり確認が必要だった。

IN = iter(Input.split('\n')).__next__
def input():
    return IN()

N = int(input())
A = [list(map(int,list(input()))) for _ in range(N)]

max_A = 0
# print(A)
for i in range(N):
    for j in range(N):
        print(i,j)
        if A[i][j] > max_A:
            max_A_idx=[[i,j]]
            max_A = A[i][j]
        elif A[i][j] == max_A:
            max_A_idx.append([i,j])
# print(max_A)
# print(max_A_idx)
for i in range(len(max_A_idx)):
    res = str(max_A)
    idx_x = max_A_idx[0]
    idx_y = max_A_idx[1]
    for j in range(N):
        next_max = 0
        next_max_idx = []
        for k in [[1,0],[0,1],[-1,0],[0,-1],[1,1],[1,-1],[-1,1],[-1,-1]]:
            next_idx_x = idx_x+k[0]
            next_idx_y = idx_y+k[1]
            if next_max < A[next_idx_x][next_idx_y]:
                next_max = A[next_idx_x][next_idx_y]
                next_max_idx.append([next_idx_x, next_idx_y])
            
        res += next_max