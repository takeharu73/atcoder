N,A,B = list(map(int,input().split()))
 
for i in range(N):
    if i%2==0:
        for j in range(A):
            if N%2==0:
                print(("."*B+"#"*B)*(int(N)//2))
            else:
                print(("."*B+"#"*B)*(int(N)//2) + "."*B)
    else:
        for j in range(A):
            if N%2==0:
                print(("#"*B+"."*B)*(int(N)//2))
            else:
                print(("#"*B+"."*B)*(int(N)//2) + "#"*B)