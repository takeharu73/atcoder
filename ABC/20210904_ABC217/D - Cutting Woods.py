"""
Time Limit ExceededエラーのためACならず。
"""

L, Q = map(int, input().split())
C, X = [],[]
for i in range(Q):
    c, x = map(int, input().split())
    C.append(c)
    X.append(x)

l_len = [L]

for i,[c,x] in enumerate(list(zip(C,X))):
    all_len = 0
    if c ==1:
        # xが何番目の木なのかを判別する
        for j in range(len(l_len)):
            if x<l_len[j]:
                break
        # x_indexに切った後の左の長さまでの合計を代入、x_index+1に右の長さまでの合計をinsertする
        l_len.insert(j+1, l_len[j])
        l_len[j] = x

    elif c==2:
        for j in range(len(l_len)):
            if x<l_len[j]:
                if j != 0:
                    print(l_len[j]-l_len[j-1])
                else:
                    print(l_len[j])
                break