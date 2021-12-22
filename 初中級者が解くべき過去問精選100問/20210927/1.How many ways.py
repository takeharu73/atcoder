n, x = list(map(int, input().split()))
# 3 ≤ n ≤ 100
# 0 ≤ x ≤ 300
res = 0
for i in range(1, x-2):
    for j in range(i+1, int((x-i)/2)):
        if i !=j and i!= (x-i-j-1) and j!= (x-i-j-1):
            print(i,j,x-i-j-1)
            
            res += 1
print(res)