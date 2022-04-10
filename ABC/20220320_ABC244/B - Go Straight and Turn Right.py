N = int(input())
T = input()
 
p = 0
xy = [0,0]
P = [[1,0],[0,-1],[-1,0],[0,1]]
for t in T:
    if t == "S":
        xy[0] += P[p][0]
        xy[1] += P[p][1]
    elif t=="R":
        if p!=3:
            p+=1
        else:
            p=0
print(xy[0], xy[1])