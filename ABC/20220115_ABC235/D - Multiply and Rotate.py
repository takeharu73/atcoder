# ★部分に気づけず、WA（All 17/19がAC、2/19がWA）

from collections import deque

a, N = list(map(int, input().split()))

path = {}
# BFS 
# 探索対象 node を queue （キュー）に入れる。
queue = deque()
# 本問では node N から探索を開始するため queue に node N を最初に入れる
# queue.append(1)
queue.append(N)
# queue がなくなるまで探索を続ける
visited = set()
flg = 0
while queue:
    # queue から node を 1 つ取り出す。取り出したノードについて調べる。
    # 取り出された node は queue から消える。
    node = queue.popleft() # .pop() にすると DFS になる
    
    if node==1:
        flg = 1
        break    
    
    node_s = str(node)
#     print(node) # コメントアウトを外すと現在地がわかる。
    # 取り出された node の隣接 node 達を nears に入れる。
    nears = []
    if node%a == 0:
        nears.append(int(node/a))

    # ★ここがWAの原因。106→61になってしまう。本当は061なので、このパターンは認められない。
    # ★WAを回避するには、以下のように2桁目が0の場合を考慮するように修正する必要があった。
    # if node_s[-1]!="0":
    if node_s[-1]!="0" and len(node_s)>1 and node_s[1]!="0":
        node_s = node_s[1:]+node_s[0]
        nears.append(int(node_s))
    
    # 隣接 node 達が探索済みか 1 つずつ調べる。
    for near in nears:
        # 未探索の隣接 node は queue に追加する。
        # 取り出してきた親 node は子nearの道しるべとなるため、path[near]に追加する。
        if near not in visited:
            queue.append(near)
            path[near] = node
            visited.add(near)

if flg == 0:
    print(-1)    
else:
    n = 1
    res = 0
    while True:
        n = path[n]
        res += 1
        if n==N:
            break
    print(res)