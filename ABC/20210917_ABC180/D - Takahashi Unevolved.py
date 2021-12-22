X,Y,A,B = map(int, input().split())
res = 0
flg_A = 0
while True:
    if flg_A == 0:
        if (A-1)*X>B:
            flg_A = 1
            
    if flg_A == 1:
        res+=(Y-X-1)//B
        break
    else:
        X*=A
        if X>=Y:
            print(res)
            break
        res+=1
if flg_A == 1:
    print(res)