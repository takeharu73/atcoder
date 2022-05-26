N = int(input())
S=[]
T=[]
 
for i in range(N):
    ints = input().split()
    S.append(ints[0])
    T.append(int(ints[1]))
# print(S)
 
dic = {}
res = 0
for i in range(N):
    if dic.get(S[i]) is None:
        dic[S[i]] = T[i]
        if res < T[i]:
            res = T[i]
            res_idx = i+1
 
print(res_idx)