IN = iter(Input.split('\n')).__next__
def input():
    return IN()

N,W = map(int,input().split())

dp = [-1]*(W+1)
dp[0] = 0

# dp[i]を、「重さの合計がw以下になるように複数個選ぶことを許して選んだ場合の合計価値の最大値」とする。
# すると、dp[i+1]=max(dp[i],dp[i−weight]+value)が成り立つ
# 今回漸化式の中に1変数が存在（重さ）するため、DPは1次元リストで初期化
# N個の商品に対して上記の式をloopを回すことで（累積和）、高速処理を実現している

for loop in range(N):
#     print(dp)
    value,weight = map(int,input().split())
    for i in range(weight,W+1):
        if dp[i-weight] == -1:
            pass
        else:
            dp[i] = max(dp[i],dp[i-weight]+value)
# print(dp)

# 上の処理にて、入力がN=4, W=8, VW=[[4, 2], [5, 2], [2, 1], [8, 3]]の時、dpは以下のように更新される。
# [0, -1, -1, -1, -1, -1, -1, -1, -1]
# [0, -1, 4, -1, 8, -1, 12, -1, 16]
# [0, -1, 5, -1, 10, -1, 15, -1, 20]
# [0, 2, 5, 7, 10, 12, 15, 17, 20]
# [0, 2, 5, 8, 10, 13, 16, 18, 21]        

print(max(dp))