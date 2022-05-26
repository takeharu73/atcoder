N,Q = list(map(int,input().split()))
X = [int(input()) for _ in range(Q)]
N_list = [i+1 for i in range(N)]
 
# print(X)
 
# 数: index
dic1 = dict(zip(N_list,N_list))
# index: 数
dic2 = dict(zip(N_list,N_list))
 
# print(dic2)
# print(X)
for i,x in enumerate(X):
    if dic1[x] == N:
        tmp2 = dic1[x]
        dic1[x] = dic1[x]-1
#         tmp = dic2[i]
        tmp = dic2[dic1[x]]
#         print(tmp)
        dic2[dic1[x]] = x
#         dic2[i+1] = tmp
        dic2[dic1[x]+1] = tmp
        dic1[tmp] = tmp2
    else:
        tmp2 = dic1[x]
        dic1[x] = dic1[x]+1
#         tmp = dic2[i+2]
        tmp = dic2[dic1[x]]
#         print(tmp)
        dic2[dic1[x]] = x
#         dic2[i+1] = tmp
        dic2[dic1[x]-1] = tmp
        dic1[tmp] = tmp2
#     print(dic1, dic2)
#     print(list(dic2.values()))
res = list(map(str, list(dic2.values())))
print(" ".join(res))