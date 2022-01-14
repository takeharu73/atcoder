# 2進法の1を2に変換すれば答えというのに気づけず沢山時間をかけてしまった。反省。
# 考えられるパターンは可視化していたので気付きたかった。

"""
2
20
22
200
202
220
222
2000
2002
2020
2022
2200
2202
2220
2222
20000
20002
20020
20022
20200
20202
20220
20222
22000
22002
22020
22022
22200
22202
22220
22222
...


1
2
4
8
16

"""
K = int(input())
 
from operator import mul
from functools import reduce
 
def cmb(n):
    return 2**n
 
 
total = 0
i = 0
while True:
    if K <= total:
        total -= cmb(i-1)
        break
    else:
        total += cmb(i)
        i+=1
 
remain = K-total-1
res = []
for k in range(i-2,-1,-1):
    if k == 0:
        if remain == 0:
            res.append("0")
        else:
            res.append("2")
    else:
        remain -= 2**k
        if remain >=0:
            res.append("2")
        else:
            remain += 2**k
            res.append("0")
 
print("2"+"".join(res))