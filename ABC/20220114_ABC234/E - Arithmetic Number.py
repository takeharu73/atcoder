X = int(input())
 
# 6桁以上で全ての桁が同じ数字でないもの
ar = [123456,234567,345678,456789,543210,654321,765432,876543,987654,1234567,2345678,3456789,6543210,7654321,8765432,9876543,12345678,23456789,76543210,87654321,98765432,123456789,876543210,987654321,9876543210]
 
# 5桁までで全ての桁が同じ数字でないもの
for i in range(2,6):
    # 1桁目の数字
    for j in range(10):
        # 差分
        for k in range(-9,10,1):
            if 0<=j+k*(i-1)<=9:
                num_l = []
                num_l.append(str(j))
                for n in range(1, i):
                    num_l.append(str(j+k*n))
                num = int("".join(num_l))
                ar.append(num)
 
# すべて同じ数字のもの
for i in range(1,19):
    for j in range(10):
        ar.append(int(str(j)*i))
 
ar = sorted(ar)
 
for a in ar:
    if a >= X:
        print(a)
        break