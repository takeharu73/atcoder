R, C = list(map(int, input().split()))
a = [list(map(int, input().split())) for _ in range(R)]
 
def reverse_row(a, row):
    if row == []:
        return a
    for r in row:
        a[r] = [0 if i==1 else 1 for i in a[r]]
        return a
    
# 行数は最大10なので、O(2**10)でいける
# 列数は最大10000で、bit全探索は無理なので、各行の1の枚数が行数/2と比較してどうかで判断する（行数/2より小さければ、ひっくり返すべき）
 
res_f = 0
for i in range(2**R):
    row = []
    for j in range(R):
        if (i>>j)&1:
            row.append(j)
    a = reverse_row(a, row)
    
    res = 0
    for c in range(C):
        sum_col = sum([a_row[c] for a_row in a])
        if sum_col <= R/2:
            res += (R - sum_col)
        else:
            res += sum_col
    
    res_f = max(res_f, res)
 
print(res_f)    