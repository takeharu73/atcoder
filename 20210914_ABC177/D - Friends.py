N, M = map(int, input().split())
 
#Union Find
parent = [-1] * N
 
def root(x):
    """
    データxが属する木の根を再帰で得る
    """
    # どの木にも属していない場合
    if parent[x] < 0:
        return x
    else:
        parent[x] = root(parent[x])
        return parent[x]
 
def unite(x,y):
    """
    xとyの木を併合
    """
    x = root(x)
    y = root(y)
 
    # xとyの根が同じ(=同じ木にある)時はそのまま
    if x == y:
        return
    # xとyの根が同じでない(=同じ木にない)時：yの根をxの根につける。xのノード数(マイナス)にyのノード数(マイナス)を加算する
    else:
        parent[x] += parent[y]
        parent[y] = x
 
# 最初は全てrootノードとして初期化(-1)
# print("parent", parent)

for _ in range(M):
    a, b = map(int, input().split())
    unite(a-1, b-1)
    # print("parent", parent)
 

print(-min(parent))