N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]
 
res = 0
for i in range(N):
    xy1=XY[i]
    for j in range(i+1, N):
        xy2=XY[j]
        for k in range(j+1, N):
            xy3=XY[k]
            if xy2[1]-xy1[1]!=0 and xy3[1]-xy1[1]!=0:
                # 小数点以下の誤差のためWA
                # if (xy2[0]-xy1[0])/(xy2[1]-xy1[1]) != (xy3[0]-xy1[0])/(xy3[1]-xy1[1]):
                # Fractionを使い誤差をなくすようにしたが、TLE（かかる時間が10倍くらいになった）
                # if Fraction(xy2[0]-xy1[0])/(xy2[1]-xy1[1]) != Fraction(xy3[0]-xy1[0])/(xy3[1]-xy1[1]):
                # Decimalも、TLE（さらに時間が伸びた）
                # if Decimal(xy2[0]-xy1[0])/(xy2[1]-xy1[1]) != Decimal(xy3[0]-xy1[0])/(xy3[1]-xy1[1]):

                # 小数点以下の誤差がある場合、「例えばx/y=z/aなら両辺にyとaをかけて、xa=zyとするとよい」とのアドバイスから、以下のように変更しAC
                if (xy2[0]-xy1[0])*(xy3[1]-xy1[1]) != (xy3[0]-xy1[0])*(xy2[1]-xy1[1]):
                    res += 1
                    
            else:
                if xy2[1]-xy1[1]!=0 or xy3[1]-xy1[1]!=0:
                    res+=1
print(res)        