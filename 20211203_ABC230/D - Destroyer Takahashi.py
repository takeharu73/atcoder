# 破壊される壁をpopしなくても、N回ループで正しく計算できることに気づけず、popを行ったところO(N^2)でTLE。
# 実装は簡単。

N,D = list(map(int, input().split()))
LR = []
for _ in range(N):
    lr = list(map(int, input().split()))
    LR.append(lr)
    
LR = sorted(LR, key=lambda x: x[1])
 
res = 0
right = 0
for i in range(len(LR)):
    if right < LR[i][0]:
        right = LR[i][1]+D-1
        res += 1
print(res)