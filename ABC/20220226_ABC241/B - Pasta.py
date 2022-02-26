N, M = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))
 
# print(A)
# print(B)
flg_a = 0
for i, b in enumerate(B):
    if flg_a == 1:
        break
    flg = 0
    for j,a in enumerate(A):
        if a == b:
            A.pop(j)
#             print(A)
            flg = 1
            break
    if flg==0:
        print("No")
        flg_a = 1
        break
 
            
if flg_a == 0:
    print("Yes")