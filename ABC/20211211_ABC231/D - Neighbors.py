N,M = list(map(int, input().split()))
AB = []
for i in range(M):
    ab = list(map(int,input().split()))
    ab[0] -= 1
    ab[1] -= 1
    AB.append(ab)
# print(AB)
 
from collections import defaultdict
 
class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n
 
    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
 
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
 
        if x == y:
            return
 
        if self.parents[x] > self.parents[y]:
            x, y = y, x
 
        self.parents[x] += self.parents[y]
        self.parents[y] = x
 
    def same(self, x, y):
        return self.find(x) == self.find(y)
 
    
dic = {}
flg = 0
uf = UnionFind(N)
if M>=N:
    print("No")
    flg = 1
else:
    for a,b in AB:
        if dic.get(a):
            dic[a]+=1
            if dic[a]>=3:
                print("No")
                flg = 1
                break
        else:
            dic[a]=1
        if dic.get(b):
            dic[b]+=1
            if dic[b]>=3:
                print("No")
                flg = 1
                break
        else:
            dic[b]=1
        
        if uf.same(a,b):
            print("No")
            flg = 1
            break         
        else:
            uf.union(a, b)
 
if flg == 0:
    print("Yes")