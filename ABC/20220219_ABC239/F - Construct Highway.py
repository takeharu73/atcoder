# Union-findに気づき、惜しいところまでいくが、実装力が足りず時間切れ
# Eをやればよかった・・。Eは1つずつ葉から計算していけばよいことは気付いたが、再帰に気付けず。
# Eはオイラーツアーで解ける問題。https://qiita.com/recuraki/items/72e37eb9be9f71bc623a

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
    
N, M = list(map(int, input().split()))
D = list(map(int, input().split()))
AB = [list(map(int, input().split())) for _ in range(M)]
AB = [[a-1, b-1] for a, b in AB]
uf = UnionFind(N)
honsu = [0]*N

flg_same = 0
for a, b in AB:
    # aとbがすでに同じunionの場合、flg_sameを1にする
    if uf.same(a,b):
        flg_same=1
    uf.union(a, b)
    honsu[a]+=1
    honsu[b]+=1

nokori = []
for i, d in enumerate(D):
    nokori.append(d-honsu[i])

dic_uf = dict(uf.all_group_members())
nokori_uf = []
nokori_uf_node = []
for U, V in dic_uf.items():
    nokori_u = 0
    nokori_uf_node_each = []
    for v in V:
        if nokori[v]>=1:
            nokori_u+=nokori[v]
            nokori_uf_node_each.extend([v+1]*nokori[v])
    nokori_uf.append(nokori_u)
    nokori_uf_node.append(nokori_uf_node_each)

import collections
count = collections.Counter(nokori_uf)

index_1 = []
for i, n in enumerate(nokori_uf):
    if n==1:
        index_1.append(i)
print(count)
all_count = 0
for c, n in dict(count).items():
    all_count += c*n
if all_count != 2*len(dic_uf.keys())-2 or 0 in count.keys():
    print(-1)
else:
    first = nokori_uf_node.pop(index_1[1])[0]
    last = nokori_uf_node.pop(index_1[0])[0]
    nokori_uf.pop(index_1[1])
    nokori_uf.pop(index_1[0])
    nokori_uf_node = sorted(nokori_uf_node, key=len, reverse=True)
    # print("nokori_uf_node", nokori_uf_node)   
    right_id = len(nokori_uf_node)-1
    while True:
        print(nokori_uf_node, right_id)
        left = nokori_uf_node[0].pop(0)
        right = nokori_uf_node[right_id].pop(0)
        if nokori_uf_node[right_id] == []:
            nokori_uf_node.pop(right_id)
        if nokori_uf_node[0] == []:
            nokori_uf_node.pop(0)
            right_id = len(nokori_uf_node)
        right_id -= 1
        print(left, right)
        if nokori_uf_node == []:
            break