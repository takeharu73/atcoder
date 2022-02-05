N = int(input())
A = list(map(int,input().split()))

B = []
# print(A)
sum_p = 0
flg = 0
for a in A:
    sum_p += a
    if sum_p > 360:
        flg = 1
        sum_p -= 360
    B.append(sum_p)
#     print(B)
if flg == 0:
    B.append(360)

res = []
i=0
B = sorted(B)
# print(B)
for b in B:
    if i == 0:
        prev_b = b
        res.append(b)
    else:
        res.append(b-prev_b)
        prev_b = b
    i+=1
print(max(res))