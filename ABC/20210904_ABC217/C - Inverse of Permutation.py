N = int(input())
p = list(map(int, input().split()))

l=[0]*N
for i in range(N):
    l[p[i]-1]=str(i+1)
print(" ".join(l))