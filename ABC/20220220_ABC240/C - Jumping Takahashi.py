# DPに気づけずTLE。bit全探索で愚直にやろうとしてしまった。

N, X = list(map(int, input().split()))
AB = [list(map(int, input().split())) for _ in range(N)]
 
A_sum = 0
B_sum = 0
B_minus_A = []
for a,b in AB:
    A_sum+=a
    B_sum+=b
    B_minus_A.append(b-a)
 
remain = X - A_sum
# print(remain)
# print(B_minus_A)
flg = 0
n = len(B_minus_A)
for i in range(2 ** n):
    bag = []
#     print("pattern {}: ".format(i), end="")
    for j in range(n):  # このループが一番のポイント
        if ((i >> j) & 1):  # 順に右にシフトさせ最下位bitのチェックを行う
            bag.append(B_minus_A[j])  # フラグが立っていたら bag に果物を詰める
    if sum(bag) == remain:
        print("Yes")
        flg = 1
if flg == 0:
    print("No")