N,K= list(map(int, input().split()))
S = []
for i in range(N):
    S.append(input())
 
res = 0 
for i in range(2 ** N):
    bag = []
    for j in range(N):
        if ((i >> j) & 1):
            bag.append(S[j])
    dic = {}
    for s in bag:
        for ss in list(set(s)):
            if dic.get(ss):
                dic[ss] += 1
            else:
                dic[ss] = 1
    res = max(list(dic.values()).count(K), res)
    
print(res)    