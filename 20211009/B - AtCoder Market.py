import math
 
N = int(input())
XY = []
for i in range(N):
    xy = input()    
    XY.append(list(map(int, xy.split())))
 
X_sum = 0
Y_sum = 0
 
X, Y = [], []
for x, y in XY:
    X.append(x)
    Y.append(y)
ent = [sorted(X)[N//2-1], sorted(X)[N//2]]
exit = [sorted(Y)[N//2-1], sorted(Y)[N//2]]
 
res_min = math.inf
for en in ent:
    for ex in exit:
        res = 0
        for x, y in XY:
            res += abs(x-en)+(y-x)+abs(ex-y)
        if res<res_min:
            res_min = res
    
print(res_min)