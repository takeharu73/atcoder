N,M,X,T,D = list(map(int,input().split()))
# query = [list(map(int,input().split())) for _ in range(Q)]
 
if M>=X:
    print(T)
else:
    print((T-X*D)+D*M)