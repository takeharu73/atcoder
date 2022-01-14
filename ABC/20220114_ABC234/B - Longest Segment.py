N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]
 
res = 0
for i in range(len(XY)):
    for j in range(i+1, len(XY)):
        dis = ((XY[i][0]-XY[j][0])**2 + (XY[i][1]-XY[j][1])**2)**(1/2)
#         print(dis)
        if res < dis:
            res = dis
print(res)