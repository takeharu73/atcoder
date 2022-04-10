N,K = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))
 
A_B = [A[0]]
B_A = [B[0]]
A_A = [A[0]]
B_B = [B[0]]
 
dp_a = [0]*N
dp_b = [0]*N
 
for i in range(1,N):
    A_B.append(abs(A[i]-B[i-1]))
    B_A.append(abs(B[i]-A[i-1]))
    A_A.append(abs(A[i]-A[i-1]))
    B_B.append(abs(B[i]-B[i-1]))
    
dp_a[0] = 1
dp_b[0] = 1
    
for i in range(N):
    if dp_a[i-1]==1:
        if A_A[i] <= K:
            dp_a[i] = 1
        if B_A[i] <= K:
            dp_b[i] = 1
    if dp_b[i-1]==1:
        if A_B[i] <= K:
            dp_a[i] = 1
        if B_B[i] <= K:
            dp_b[i] = 1
    
if dp_a[-1]==1 or dp_b[-1]==1:
    print("Yes")
else:
    print("No")