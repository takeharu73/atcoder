N  = int(input())
S  = [input() for _ in range(N)]
 
min_res = 99999999999
for i in range(10):
    res = 0
    idx = 0
    ok = []
    while True:
        if len(ok) == N:
            break
        else:
            for j, s in enumerate(S):
                # まだリールが止まっていない場合
                if j not in ok:
                    # 今のリールが欲しい数字なら
                    if int(s[idx]) == i:
                        ok.append(j)
                        if len(ok) == N:
                            break
#                         res += 1
#                         idx += 1
#                         if idx == 10:
#                             idx = 0
                        break
            if len(ok) == N:
                break
 
            res += 1
            idx += 1
            if idx == 10:
                idx = 0
#     print(res)
#     print(i, ok, res)
    if res < min_res:
        min_res = res
 
print(min_res)