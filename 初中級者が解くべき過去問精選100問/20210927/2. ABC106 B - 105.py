N = int(input())

res = 0
for i in range(N+1):
    r = 0
    if i%2 == 0:
        continue
    else:
        for j in range(1, i+1):
            if i%j==0:
                r+=1
        if r==8:
            res+=1
print(res)