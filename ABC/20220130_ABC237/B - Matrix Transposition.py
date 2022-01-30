H, W = list(map(int,input().split()))
A = [list(input().split()) for _ in range(H)]

tr = []
for i in range(W):
    tr_row = []
    for vector in A:
        tr_row.append(vector[i])
    tr.append(tr_row)    
for i in range(W):
    print(" ".join(tr[i]))