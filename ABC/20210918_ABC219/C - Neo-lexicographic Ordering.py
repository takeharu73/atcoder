X = list(input())
dic = {}
for i, x in enumerate(X):
    dic[x]=i
N = int(input())
S = [input() for _ in range(N)]
 
res = {}
for s in S:
    r = 0
    k = 0
    for c in s[::-1]:
        r += 26**k*dic[c]
        k += 1
    res[s]=r
 
res = sorted(res.items(), key=lambda x:x[1], reverse=False)
for r in res:
    print(r[0])