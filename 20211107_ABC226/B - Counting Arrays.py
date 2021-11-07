import collections
 
N = int(input())
L = set()
for i in range(N):
#     l, *a = list(map(int, input().split()))
    a = input()
    L.add(a)
 
print(len(L))