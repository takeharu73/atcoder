N, K, A = map(int, input().split())
# print(N, K, A)
if N ==1:
    print(1)
else:
    a = ((K-1)%N+A)%N
    if a == 0:
        print(N)
    else:
        print(a if a<=N else a-N)