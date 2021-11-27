A,B = input().split()
a = list(A)
b = list(B)
flg = 0
for i in range(len(a)):
    if len(b) > i:
        if int(a[-(i+1)]) + int(b[-(i+1)]) >= 10:
            print("Hard")
            flg = 1
            break
if flg == 0:
    print("Easy")