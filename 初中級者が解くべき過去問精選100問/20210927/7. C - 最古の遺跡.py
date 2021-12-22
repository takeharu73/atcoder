# 以下の解法だとMLEになる。

N = int(input())
# 同じ点は存在しない制約のため、メモリ節約のためsetだけにする
XY_s = set()
for i in range(N):
    xy = input()
    XY_s.add(xy)

del xy

# N<=3000 → O(N^2)まで
# 2点を固定すると、考えられる正方形は2つに絞り込まれるため、それらが存在するかをチェックすれば、O(N^2)で最大の正方形が求まる

def cal_coordinate(xy1,xy2):
    x1, y1 = xy1
    x2, y2 = xy2
    x3, y3 = x2-y1+y2, y2+x1-x2
    x4, y4 = x1-y1+y2, y1+x1-x2

    return([str(x3),str(y3)],[str(x4),str(y4)])

max_area = 0
for i, xy1 in enumerate(XY_s):
    for j, xy2 in enumerate(XY_s):
        if j>i:
            x1,y1 = list(map(int, xy1.split()))
            x2,y2 = list(map(int, xy2.split()))
            xy3,xy4 = cal_coordinate([x1,y1],[x2,y2])
            if " ".join(xy3) in XY_s and " ".join(xy4) in XY_s:
                area = round((((x1-x2)**2+(y1-y2)**2)**(1/2))**2)
                if area > max_area:
                    max_area = area
                area = 0

print(max_area)