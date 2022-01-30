import itertools
N = int(input())
S = input()
from collections import deque
A = deque([])
lenS = len(S)
A.appendleft(deque([str(lenS)]))

for i,s in enumerate(S[::-1]):
    if s=="R":
        A[0].appendleft(str(lenS-i-1))
    else:
        A.append(deque([str(lenS-i-1)]))
        A.appendleft(deque([]))
    
l_2d = [list(a) for a in A if a]
print(" ".join(list(itertools.chain.from_iterable(l_2d))))