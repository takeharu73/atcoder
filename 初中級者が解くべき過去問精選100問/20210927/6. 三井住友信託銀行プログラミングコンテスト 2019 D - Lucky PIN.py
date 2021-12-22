N = int(input())
S = input()
# 4≤N≤30000　→O(N^2)だと厳しい

# 1〜3桁目のそれぞれに0〜9のうち選べうる数字の個数を調べられれば、答えが出る
# 10*10*10のリストを作成し、左からN桁繰り返し1回で、リストを埋めれば良い

l_1 = [0]*10
l_2 = [[0] * 10 for i in range(10)]
l_3 = [[[0] * 10 for i in range(10)] for j in range(10)]

for s in S:
    for i in range(10):
        if l_1[i] == 1:
            for j in range(10):
                if l_2[i][j] == 1:
                    if l_3[i][j][int(s)] == 0:
                        l_3[i][j][int(s)] = 1
            if l_2[i][int(s)] == 0:
                l_2[i][int(s)] = 1
    if l_1[int(s)] == 0:
        l_1[int(s)] = 1

res = 0
for i in range(10):
    for j in range(10):
        for k in range(10):
            if l_3[i][j][k] == 1:
                res += 1
print(res)