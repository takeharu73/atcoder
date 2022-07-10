N, K, Q = list(map(int,input().split()))
A = list(map(int,input().split()))
A = [a-1 for a in A]
L = list(map(int,input().split()))
L = [l-1 for l in L]
 
# print(A)
for i in range(Q):
    if A[L[i]]!=N-1:
        if L[i] != K-1:
            if A[L[i]]+1 != A[L[i]+1]:
                A[L[i]] = A[L[i]]+1
#                 print(A)
        else:
            A[L[i]] = A[L[i]]+1
#             print(A)
 
A = [str(a+1) for a in A]
print(" ".join(A))