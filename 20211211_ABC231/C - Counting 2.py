import bisect
 
N,Q = list(map(int, input().split()))
A = list(map(int,input().split()))
A = sorted(A)
A = [a+1 for a in A]
X = []
for i in range(Q):
    X.append(int(input()))
    
for x in X:
    print(len(A)-bisect.bisect(A,x))