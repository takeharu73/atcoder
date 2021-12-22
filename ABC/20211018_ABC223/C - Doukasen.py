from collections import deque
 
N = int(input())
AB = deque([list(map(int, input().split())) for _ in range(N)])
 
AB_time = deque([a/b for a,b in AB])
 
time, left, right = 0, 0, 0
while True:
    if len(AB_time) == 1:
        left += AB[0][0]/2
        print(left)
        break
    elif AB_time[0]<AB_time[-1]:
        left += AB[0][0]
        AB_time[-1] -= AB_time[0]
        AB[-1][0] -= AB_time[0]*AB[-1][1]
        AB_time.popleft()
        AB.popleft()
    elif AB_time[0]>AB_time[-1]:
        left += AB[0][1]*AB_time[-1]
        AB_time[0] -= AB_time[-1]
        AB[0][0] -= AB[0][1]*AB_time[-1]
        AB_time.pop()
        AB.pop()
    elif AB_time[0]==AB_time[-1]:
        if len(AB) == 2:
            left += AB[0][0]
            print(left)
            break
        else:
            left += AB[0][0]
            AB_time.popleft()
            AB_time.pop()
            AB.popleft()
            AB.pop()