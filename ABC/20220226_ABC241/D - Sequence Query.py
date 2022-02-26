# 愚直に解こうとしてTLE
# 二分探索やwavelet matrix等のキーワードは思いついていたが、実装できず時間切れ。
# multisetの考え方、学びたい→https://tsubo.hatenablog.jp/entry/2020/06/15/12465→

N = int(input())
Q = [list(map(int, input().split())) for _ in range(N)]

A = {}
for q in Q:
    if q[0] == 1:
        if A.get(q[1]):
            A[q[1]] += 1
        else:
            A[q[1]] = 1
    elif q[0]==2:
        res = 0
        flg = 0
        keys_a = set(A.keys())
        keys = set()
        for key in keys_a:
            if key <= q[1]:
                keys.add(key)
#         print(A,keys)
                
        for key in list(keys)[::-1]:
            res += A[key]
            if res >= q[2]:
                print(key)
                flg = 1
                break
        if flg == 0:
            print(-1)
    elif q[0]==3:
        res = 0
        flg = 0
        keys_a = set(A.keys())
        keys = set()
        for key in keys_a:
            if key >= q[1]:
                keys.add(key)
#         print(A,keys)
        for key in list(keys):
            res += A[key]
#             print("res", res, "k", k)
            if res >= q[2]:
                print(key)
                flg = 1
                break
        if flg == 0:
            print(-1)