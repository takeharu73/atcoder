N = int(input())
A = list(map(int,input().split()))
 
res = 0
am = 0
for i in range(3):
    res += A[-(i+1)]
    if res>=4:
        break
    else:
        am += 1
 
print(N-am)