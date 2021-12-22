N = int(input())
XY = []
for i in range(N):
    XY.append(list(map(int, input().split())))
 
AB = []
 
for x1, y1 in XY:
    ab = []
    for x2, y2 in XY:
        if x1-x2 != 0 or y1-y2 != 0:
            ab.append([x1-x2, y1-y2])
    AB.append(ab)
 
res = set()
import math
for ab in AB:
    for aabb in ab:
        m = math.gcd(*aabb)
        aabb[0]=int(aabb[0]/m)
        aabb[1]=int(aabb[1]/m)
        s = str(aabb[0])+" "+str(aabb[1])
        if s not in res:
            res.add(s)
 
print(len(res))