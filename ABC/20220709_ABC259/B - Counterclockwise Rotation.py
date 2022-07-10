a,b,d = list(map(int,input().split()))
# query = [list(map(int,input().split())) for _ in range(Q)]
 
import math
cos = math.cos(math.radians(d))
sin = math.sin(math.radians(d))
 
rot_x = (a * cos) - (b * sin)
rot_y = (a * sin) + (b * cos)
 
print(rot_x,rot_y)