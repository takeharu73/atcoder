N,Q = list(map(int, input().split()))
A = list(map(int, input().split()))
A_dic = {}
for i,a in enumerate(A):
    if A_dic.get(a) is None:
        A_dic[a] = [i]
    else:
        A_dic[a].append(i)
XK = [list(map(int, input().split())) for _ in range(Q)]

# print(A_dic)
# print(XK)

for xk in XK:
    if A_dic.get(xk[0]) is None or len(A_dic[xk[0]])<xk[1]:
        print(-1)
    else:
        print(A_dic[xk[0]][xk[1]-1]+1)