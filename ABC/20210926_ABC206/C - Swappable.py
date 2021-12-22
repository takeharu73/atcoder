N = int(input())
A = list(map(int, input().split()))
 
# nC2-a_1C2-a_2C2-...-a_kC2(a: 同じ値の数　k: 同じ値の組み合わせの数)
# N≤3×10^5
 
dic = {}
# O(N)
for a in A:
    if dic.get(a) is None:
        dic[a]=1
    else:
        dic[a]+=1
# print(dic)
 
res = int(N*(N-1)/2)
for d in dic.items():
    res -= int(d[1]*(d[1]-1)/2)
 
print(res)