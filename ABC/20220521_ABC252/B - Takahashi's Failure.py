N,K  = list(map(int, input().split()))
A  = list(map(int, input().split()))
B  = list(map(int, input().split()))
 
max_A = max(A)
L = []
for i,a in enumerate(A):
    if max_A == a:
        L.append(i+1)
 
flg = 0
for l in L:
    if l in B:
        print("Yes")
        flg = 1
        break
if flg == 0:
    print("No")