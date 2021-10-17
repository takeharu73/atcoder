IN = iter(Input.split('\n')).__next__
def input():
    return IN()

n = int(input())
A = list(map(int, input().split()))
q = int(input())
m = list(map(int, input().split()))

bi = 2**n
res = [0]*q
for i in range(bi):
    total = 0
    for j in range(n):
        if (i>>j) & 1:
            total += A[j]
    for k in range(q):
        if total == m[k]:
            res[k] = 1

for r in res:
    if r == 1:
        print("yes")
    else:
        print("no")