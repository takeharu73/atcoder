# バグが取り切れず、WA（バグの原因は不明）。

N = int(input())
S = list(input())

# 入力：snwfafwipeusiwkzo
# 答え：effwpnwipsusiwkzo

# 後ろから順に、最小のものを探す(1)→見つけたら先頭と交換→
                #次に最小のものを(1)よりも左から探す→見つけたら先頭+1と交換→…

idx_right = len(S)-1
idx = -1
S = S[::-1]
print(S)
for char in list("abcdefghijklmnopqrstuvwxyz"):
    for i, s in enumerate(S):
        if i <= idx:
            continue
        if i >= idx_right:
            continue
        if s==char:
            idx = i
            while True:
                if S[idx_right] <= char:
                    idx_right -= 1
                else:
                    break
                if idx_right <= i:
                    break
            print(i, idx_right, S[i], S[idx_right], char)
            if idx_right <= i:
                break
            S[i]=S[idx_right]
            S[idx_right]=char
            print(S)
            idx_right = idx_right-1
print("".join(S[::-1]))
