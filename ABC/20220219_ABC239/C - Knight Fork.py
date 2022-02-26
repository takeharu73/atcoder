flg = 0
x1, y1, x2, y2 = list(map(int, input().split()))
def route_5(x,y):
    xy = []
    xy.append([x+1, y+2])
    xy.append([x+2, y+1])
    xy.append([x-1, y-2])
    xy.append([x-2, y-1])
    xy.append([x+1, y-2])
    xy.append([x+2, y-1])
    xy.append([x-1, y+2])
    xy.append([x-2, y+1])
    return xy

XY = route_5(x1, y1)

all_XY = []
# print(XY)
for x,y in XY:
#     print(xy)
    route_xy = route_5(x,y)
    for xx, yy in route_xy:
        all_XY.append([xx, yy])
# print(all_XY)

for x,y in all_XY:
#     print(xy)
    if x==x2 and y==y2:
        print("Yes")
        flg = 1
        break
    
if flg == 0:
    print("No")