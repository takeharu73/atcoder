IN = iter(Input.split('\n')).__next__
def input():
    return IN()

A, B, C = list(map(int, input().split()))
flg = 0
for i in range(1, B//C+1):
    if i*C >= A:
        print(i*C)
        flg = 1
        break
if flg ==0:
    print(-1)
