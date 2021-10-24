from collections import deque
 
S = deque(list(input()))
 
def left_shift(S):
    s_first = S[0]
    s_last = S[-1]
    S.popleft()
    S.append(s_first)
    return "".join(S)
 
S_min, S_max = "".join(S), "".join(S)
for i in range(len(S)):
    S_up = left_shift(S)
    if S_up < S_min:
        S_min = S_up
    if S_up > S_max:
        S_max = S_up
 
print(S_min)
print(S_max)