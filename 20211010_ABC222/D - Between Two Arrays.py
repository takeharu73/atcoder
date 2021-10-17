N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 2重リストの初期化、下のミスをしたので、注意！！！
# 参考：https://note.nkmk.me/python-list-initialize/→「2次元配列（リストのリスト）を初期化する際の注意」
# DP = [[0] * 3000]*N

# 0 <= a, b <= 3000なので、3000までだとオーバーフローエラーになるミスをしたので、注意！！
# （境界値チェックはしっかりと…）
# DP = [[0] * 3000 for i in range(N)]

DP = [[0] * 3001 for i in range(N)]

for j in range(A[0], B[0]+1):
    DP[0][j] = 1
    
for i in range(1, N):
    for j in range(A[i], B[i]+1):
        # 最初の値だけは、i-1からsumで取得する必要
        if j == A[i]:
            DP[i][j] = sum(DP[i-1][A[i-1]:j+1])%998244353
        # それ以外は、DP[i][j-1]+DP[i-1][j]とすることでO(1)に計算量を押さえられる（累積和DP）←気付けず。
        # ちなみにmodで途中計算中に割るのも忘れたので、注意！！
        else:
            DP[i][j] = (DP[i][j-1]+DP[i-1][j])%998244353

        
# 最後はあまりを求める
print(sum(DP[N-1])%998244353)