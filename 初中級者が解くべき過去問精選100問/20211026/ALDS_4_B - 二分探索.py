n = int(input())
S = list(map(int, input().split()))
q = int(input())
T = list(map(int, input().split()))

# S の要素は昇順に整列されている
# n≤100,000 
# q≤50,000

import bisect

res = 0
for t in T:
    index = bisect.bisect_left(S, t)
    print(t, index, S[index])
    if index<= len(S)-1:
        if S[index] == t:
            res += 1
        
print(res)