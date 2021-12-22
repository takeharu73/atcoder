IN = iter(Input.split('\n')).__next__
def input():
    return IN()

N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]
# print(XY)

def dist(a,b):
    return ((a[0]-b[0])**2+(a[1]-b[1])**2)**0.5

Nlist = list(range(N))

import itertools
C = list(itertools.permutations(Nlist))
# print(C)
c_len_sum = 0
for c in C:
    c_len = 0
    for j in range(N-1):
#         print(c)
        c_len += dist(XY[c[j+1]], XY[c[j]])
    c_len_sum += c_len
#     print(c_len_sum)
print(c_len_sum/len(C))