##### 40分くらい。方針固めるのに時間がかかってしまった。

HW = list(map(int,input().split()))
 
"""
a b c
d e f
g h i
とすると、
a,c,e,iの4個が分かっていれば、他は一意に求まる。（本当はたぶんa,e,iの3個）
 
∵
b = HW[0]-a-c
f = HW[1]-e-d = HW[1]-e-(HW[3]-a-(HW[2]-i-(HW[4]-e-(HW[0]-a-c))))
g = HW[2]-i-h = HW[2]-i-(HW[4]-e-(HW[0]-a-c))
 
d = HW[3]-a-g = HW[3]-a-(HW[2]-i-(HW[4]-e-(HW[0]-a-c)))
h = HW[4]-e-b = HW[4]-e-(HW[0]-a-c)
c = HW[5]-i-f = HW[5]-i-(HW[1]-e-(HW[3]-a-(HW[2]-i-(HW[4]-e-(HW[0]-a-c)))))
 
"""
res = 0
for a in range(1,29):
    for c in range(1,29):
        for e in range(1,29):
            for i in range(1,29):
                if 0<HW[0]-a-c<29 and \
                0<HW[1]-e-(HW[3]-a-(HW[2]-i-(HW[4]-e-(HW[0]-a-c))))<29 and \
                0<HW[2]-i-(HW[4]-e-(HW[0]-a-c))<29 and \
                0<HW[3]-a-(HW[2]-i-(HW[4]-e-(HW[0]-a-c)))<29 and \
                0<HW[4]-e-(HW[0]-a-c)<29 and \
                c == HW[5]-i-(HW[1]-e-(HW[3]-a-(HW[2]-i-(HW[4]-e-(HW[0]-a-c))))):
                    res += 1
 
print(res)