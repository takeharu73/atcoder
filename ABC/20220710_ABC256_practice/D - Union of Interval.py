##### 二分探索で解こうとしたが、方針がよくなかった。時間がかかりすぎでギブアップ。
##### 解説AC。ソートしてから解く方法（全ての値を0から見て、区間がかぶっているもの1つでもある場合にカウントアップするやり方も面白い）

IN = iter(Input.split('\n')).__next__
def input():
    return IN()

N = int(input())
LR = [list(map(int,input().split())) for _ in range(N)]
LR = sorted(LR)    

res = 0
min_l = 0
max_r = 0
for i, lr in enumerate(LR):
    if i==0:
        min_l = lr[0]
        max_r = lr[1]
    elif max_r < lr[0]:
        res += 1
        print(min_l, max_r)
        max_r = lr[1]
        min_l = lr[0]
    else:
        if min_l > lr[0]:
            min_l = lr[0]        
        if max_r < lr[1]:
            max_r = lr[1]
    if i==len(LR)-1:
        print(min_l, max_r)