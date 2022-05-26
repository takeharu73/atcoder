# BruteForce解法しか思いつかず、TLE
# 解法としては、j全探索解法、全ての組み合わせから2個以上同じ組み合わせを除く方法、など

N  = int(input())
A  = list(map(int, input().split()))
 
dic = {}
for i, a in enumerate(A):
    if dic.get(a):
        dic[a].append(i)
    else:
        dic[a] = [i]
 
dic_n = {}
for k in dic.keys():
    n = len(dic[k])
    dic_n[k] = n
        
res = 0
dic_k = list(dic_n.keys())
for i in range(len(dic_n)):
    for j in range(i+1, len(dic_n)):
        for k in range(j+1, len(dic_n)):
            res += dic_n[dic_k[i]]*dic_n[dic_k[j]]*dic_n[dic_k[k]]
 
print(res)