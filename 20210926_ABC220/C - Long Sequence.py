%%time

IN = iter(Input.split('\n')).__next__
def input():
    return IN()

N = int(input())
A = list(map(int, input().split()))
X = int(input())

A_sum = sum(A)
# print(A_sum)
res = X//A_sum * len(A)
# print(res)
X_remain = X%A_sum
for a in A:
    X_remain -= a
    res += 1
    if X_remain<0:
        break
print(res)