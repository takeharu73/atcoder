A,B,C,X,Y = list(map(int, input().split()))
# 1≤A,B,C≤5000
# 1≤X,Y≤10^5

# # O(N^2) => TLE
# p, min_p = 0, 0
# for i in range(X+1):
#     for j in range(Y+1):
#         p = A*i+B*j+C*(max((X-i)*2, (Y-j)*2))
#         if min_p==0:
#             min_p = p
#         else:
#             if min_p>p:
#                 min_p=p
#                 l = [i,j,max((X-i)*2, (Y-j)*2)]
#         p = 0
# print(int(min_p))
# print(l)

# ABピザの枚数を決定すれば、Aピザ/Bピザの枚数は一意に定まる
# O(N) => OK
p, min_p = 0, 0
for i in range(max(X, Y)*2+1):
    p = A*(max(0,X-i/2))+B*(max(0,Y-i/2))+C*i
    if min_p==0:
        min_p = p
    else:
        if min_p>p:
            min_p=p
            l = [X-i/2,Y-i/2,i]
print(int(min_p))
