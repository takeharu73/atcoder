N,M = list(map(int,input().split()))
S = input().split()
T = set(input().split())

for s in S:
    if s in T:
        print("Yes")
    else:
        print("No")