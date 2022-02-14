# 累積和の手法に気づけず。
# 区間和といえば累積和。S[r]-S[l]=Kのやり方、覚える。
# さらにS[l]=S[r]-Kより、辞書型を1つずつ入れることで、rのループだけで十分になる。

IN = iter(Input.split('\n')).__next__
def input():
    return IN()

N, K = list(map(int, input().split()))
A = list(map(int, input().split()))

S = []
dic = {}
sum_a = 0
for a in A:
    sum_a += a
    S.append(sum_a)

# print(S)
res = 0
for r in range(N):
    if r>=1:
        if dic.get(S[r-1]):
            dic[S[r-1]] += 1
        else:
            dic[S[r-1]] = 1
    if S[r] == K:
        res += 1
    if dic.get(S[r]-K):
        res += dic[S[r]-K]
print(res)