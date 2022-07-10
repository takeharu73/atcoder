##### DPで検討したが、途中でDP不要と気付いたため、dpらしい怪しげなコードになっている。
##### また、X<Nのケースに初め気づいておらず、1WAで危うかった（コード最後の2行）

N,X= list(map(int,input().split()))
AB = [list(map(int,input().split())) for _ in range(N)]
 
# print(AB)
 
# X回クリアするのに必要な最小時間をDPとする
# dp = [0]*X
# i番目のステージを最後にクリアする場合のX回クリアするのに必要な最小時間をdpとする
# dp = [999999999999999999999999999]*N
# dp[0] = AB[0][0]
# for i in range(N):
#     dp[i] = min(dp[i]+AB[i][1], dp[i-1]+AB[i][0]+AB[i][1])
dp = [0]*N
dp[0] = AB[0][0]+AB[0][1]
for i in range(1,N):
    dp[i] = dp[i-1]+AB[i][0]+AB[i][1]
 
# print(dp)
 
for i in range(N):
    dp[i] = dp[i] + (X-i-1)*AB[i][1]
    
# print(dp)
if X>=N:
    print(min(dp))
else:
    print(min(dp[:X]))