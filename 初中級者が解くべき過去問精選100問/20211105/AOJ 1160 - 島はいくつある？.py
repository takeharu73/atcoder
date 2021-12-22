def solve():    
    def dfs(pos):
        # 訪問済の場所は0にする
        area_map[pos] = '0'
        # 次の場所を隣接するセルで1の場所から探す
        for mv in move:
            next_pos = pos + mv
            if area_map[next_pos] == '1':
                # さらにdfsを再帰的に呼び出す
                dfs(next_pos)
    
    while True:
        w, h = map(int, input().split())
        if w == 0:
            break
        
        # 陸地か否か(1/0)のマップは、area_mapに1次元で管理している
        # 外周を全て0で覆う
        area_map = ['0'] * (w + 2)
        for i in range(h):
            area_map += ['0'] + input().split() + ['0']
        area_map += ['0'] * (w + 2)
        
        move = (1, -1, w + 1, w + 2, w + 3, -w - 3, -w - 2, -w - 1)
        
        ans = 0
        # 外周を含む全ての場所に対して、陸地(1)ならばdfsを行う
        for i in range((w + 2) * (h + 2)):
            if area_map[i] == '1':
                # dfsで隣接する土地(1)はすべて0に変わる
                dfs(i)
                # 答えは島の数なので、隣接しない島がいくつあるかをansに入れる
                ans += 1
        
        print(ans)

solve()