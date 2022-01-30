S = input()

idx_left = 0
idx_right = len(S)-1

flg = 0
flg_except_a = 0
while True:
    if idx_left >= idx_right:
        break
    if S[idx_left] == S[idx_right]:
        if S[idx_left] != "a":
            flg_except_a = 1
        idx_left += 1
        idx_right -= 1
    elif S[idx_right] == "a":
        if flg_except_a == 0:
            idx_right -= 1
        else:
            flg = 1
            break
    else:
        flg = 1
        break

if flg == 0:
    print("Yes")
else:
    print("No")