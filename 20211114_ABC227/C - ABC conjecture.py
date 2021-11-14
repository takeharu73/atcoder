N = int(input())

# Python3で提出した結果、TLEに。→pypy3で提出すればOK
res = 0
# N**(1/3)等は、Nが大きくなると誤差が発生するためWA　→i*i*i>Nならbreak等として、なるべく整数を使えばOK
# for i in range(1,int(N**(1/3))+1):
#     for j in range(i,int((N/i)**(1/2))+1):
#         res += (N//(i*j))-(j-1)

# NまでとするとWA
# for i in range(1,N):
for i in range(1,N+1):
    if i*i*i>N:
        break
    # NまでとするとWA
#     for j in range(i, N):
    for j in range(i, N+1):
        if i*j*j > N:
            break
        res += (N//(i*j))-(j-1)
    
print(res)