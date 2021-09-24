IN = iter(Input.split('\n')).__next__
def input():
    return IN()

n=int(input())
x,y=map(int,input().split())

I=[]
for _ in range(n):
    a,b=map(int,input().split())
    I.append((a,b))
 

inf=10**10
dp=[[inf for i in range(y+1)] for q in range(x+1)]
dp[0][0]=0

"""
・いわゆるdp漸化式
・1つ前の状態の数値は分かっている前提で、全てのパターンを網羅的にあげることがポイント。
・ただし1つ前の状態や戦略によって取れる選択肢が変わる場合、1つ前の状態や、関係するパラメータを、漸化式の要素として入れる必要がある。
  例（https://qiita.com/keisuke-ota/items/504d66092671a67c1040より）
  ・2日連続で同じ戦略は取れない→ C問題
  ・ナップザック問題→D問題）
・添え字が1つなら、初期値はdp[0]=0だけで良いが、2つになるとdp[0][w]=0(w=1,2,...,n), 3つになると今回のようにdp[i][q]=0(i=1,2,...,x, q=1,2,...,y)が必要。 
"""

# 弁当の数だけループ
for nx,ny in I:
    # print("弁当", nx,ny)
    # 大きい方からループする理由→1つずつ弁当を与えたいが、小さい方からループしてしまうと1つ弁当が与えられた状態からさらに同じ弁当が追加で与えられる状況があり得てしまう。
    for i in range(x,-1,-1):
        for q in range(y,-1,-1):
            # 初回→i,q=(0,0)の時に、dp[nx][ny] = 1で更新
            # 以降、dp[i][q]!=infの時に、dp[min(x, i+nx)][min(y,q+ny)]を、自分自身とdp[i][q]+1のいずれか小さい方で更新（既出の弁当最小数の方が小さければそれを保持する）
            dp[min(x,i+nx)][min(y,q+ny)]= min(dp[min(x,i+nx)][min(y,q+ny)], dp[i][q]+1)

            # (確認用)
            # if dp[min(x,i+nx)][min(y,q+ny)] != inf:
                # print("更新内容", min(x,i+nx), min(y,q+ny), dp[min(x,i+nx)][min(y,q+ny)])

# 最後にdp[x][y]が更新されていれば(=与えられた弁当の組み合わせで到達できるならば)、dp[x][y]を出力、更新されていないなら-1を出力
print(dp[x][y]) if dp[x][y]<inf else print(-1)