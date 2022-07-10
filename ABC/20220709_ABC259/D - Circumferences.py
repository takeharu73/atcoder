##### 1/2乗はやってはいけないと、あれほど何度も…！！（誤差のため3WAで時間内に解けなかった）
##### 階乗を使わないように計算したら通った。。

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
 
    def size(self, x):
        return -self.parents[self.find(x)]
 
    def same(self, x, y):
        return self.find(x) == self.find(y)
 
    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]
 
    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]
 
    def group_count(self):
        return len(self.roots())
 
    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members
 
    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())
 
 
N = int(input())
sx,sy,tx,ty = list(map(int,input().split()))
XYR = [list(map(int,input().split())) for _ in range(N)]
 
for i in range(N):
    dist_s = (XYR[i][0] - sx)**2 + (XYR[i][1] - sy)**2
    dist_t = (XYR[i][0] - tx)**2 + (XYR[i][1] - ty)**2
    if dist_s == XYR[i][2]**2:
        s = i
    if dist_t == XYR[i][2]**2:
        t = i
 
# 円aと円bが接しているかを判定、接していれば同じグループに（unionfind）
# SとTが接する円が、同じグループなら、OK。違うグループなら、NG。
# N<=3000なので、N^2ですべての円について判定可能
 
def connected(xyr1, xyr2):
    dist = (xyr2[0] - xyr1[0])**2 + (xyr2[1] - xyr1[1])**2
    if dist < (xyr2[2]-xyr1[2])**2:
        return False
    elif dist > (xyr1[2] + xyr2[2])**2:
        return False
    else:
        return True
 
uf = UnionFind(N)
 
for i in range(N):
    for j in range(N):
        if connected(XYR[i], XYR[j]):
            uf.union(i, j)
 
if uf.same(s, t):
    print("Yes")
else:
    print("No")