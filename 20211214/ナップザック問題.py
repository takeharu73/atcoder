# %%time

IN = iter(Input.split('\n')).__next__
def input():
    return IN()

N, W = list(map(int, input().split()))
VW = [list(map(int, input().split())) for _ in range(N)]


#### 20211219
# dp[i]を、「i重さの合計がi以下になるように選んだ場合の合計価値の最大値」とする。
# すると、dp[i+1]=max(dp[i],dp[i-w]+v)が成り立つ
# こうすると1変数とでき（重さのみ）、DPは1次元リストで初期化でよい
# ただし商品の個数分のループは必要

dp = [-1]*(W+1)
dp[0]=0

for _, (v, w) in enumerate(VW):
    print(dp)
    for i in range(W + 1):
        if i - w >= 0 and dp[i-w]!=-1:
            dp[i] = max(dp[i], dp[i-w] + v)
print(dp)

# 上の処理にて、入力がN=4, W=5, VW=[[4, 2], [5, 2], [2, 1], [8, 3]]の時、dpは以下のように更新される。
# [0, -1, -1, -1, -1, -1]
# [0, -1, 4, -1, 8, -1]
# [0, -1, 5, -1, 10, -1]
# [0, 2, 5, 7, 10, 12]
# [0, 2, 5, 8, 10, 13]
# 13

print(max(dp))



#### 20211214
# dp[i][w]を、「i番目までの品物から重さの合計がw以下になるように選んだ場合の合計価値の最大値」とする。
# すると、dp[i+1][w]=max(dp[i][w],dp[i][w−weight[i]]+value[i])が成り立つ
# 今回漸化式の中に2変数が存在（重さと個数）するため、DPは2次元リストで初期化＆forループを2回回す
dp = [[0]*(W+1) for _ in range(N+1)]

for i, (v, w) in enumerate(VW):
    for j in range(W + 1):
        dp[i + 1][j] = dp[i][j]
        if j - w >= 0:
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j - w] + v)
#             print(dp)

# 上の処理にて、入力がN=4, W=5, VW=[[4, 2], [5, 2], [2, 1], [8, 3]]の時、dpは以下のように更新される。
# [[0, 0, 0, 0, 0, 0], [0, 0, 4, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
# [[0, 0, 0, 0, 0, 0], [0, 0, 4, 4, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
# [[0, 0, 0, 0, 0, 0], [0, 0, 4, 4, 4, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
# [[0, 0, 0, 0, 0, 0], [0, 0, 4, 4, 4, 4], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
# [[0, 0, 0, 0, 0, 0], [0, 0, 4, 4, 4, 4], [0, 0, 5, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
# [[0, 0, 0, 0, 0, 0], [0, 0, 4, 4, 4, 4], [0, 0, 5, 5, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
# [[0, 0, 0, 0, 0, 0], [0, 0, 4, 4, 4, 4], [0, 0, 5, 5, 9, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
# [[0, 0, 0, 0, 0, 0], [0, 0, 4, 4, 4, 4], [0, 0, 5, 5, 9, 9], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
# [[0, 0, 0, 0, 0, 0], [0, 0, 4, 4, 4, 4], [0, 0, 5, 5, 9, 9], [0, 2, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
# [[0, 0, 0, 0, 0, 0], [0, 0, 4, 4, 4, 4], [0, 0, 5, 5, 9, 9], [0, 2, 5, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
# [[0, 0, 0, 0, 0, 0], [0, 0, 4, 4, 4, 4], [0, 0, 5, 5, 9, 9], [0, 2, 5, 7, 0, 0], [0, 0, 0, 0, 0, 0]]
# [[0, 0, 0, 0, 0, 0], [0, 0, 4, 4, 4, 4], [0, 0, 5, 5, 9, 9], [0, 2, 5, 7, 9, 0], [0, 0, 0, 0, 0, 0]]
# [[0, 0, 0, 0, 0, 0], [0, 0, 4, 4, 4, 4], [0, 0, 5, 5, 9, 9], [0, 2, 5, 7, 9, 11], [0, 0, 0, 0, 0, 0]]
# [[0, 0, 0, 0, 0, 0], [0, 0, 4, 4, 4, 4], [0, 0, 5, 5, 9, 9], [0, 2, 5, 7, 9, 11], [0, 2, 5, 8, 0, 0]]
# [[0, 0, 0, 0, 0, 0], [0, 0, 4, 4, 4, 4], [0, 0, 5, 5, 9, 9], [0, 2, 5, 7, 9, 11], [0, 2, 5, 8, 10, 0]]
# [[0, 0, 0, 0, 0, 0], [0, 0, 4, 4, 4, 4], [0, 0, 5, 5, 9, 9], [0, 2, 5, 7, 9, 11], [0, 2, 5, 8, 10, 13]]
            
print(dp[-1][-1])