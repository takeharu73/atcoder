N,Q = list(map(int,input().split()))
S = input()
slen = len(S)
query = [list(map(int,input().split())) for _ in range(Q)]
 
# print(query)
 
# abcdefghijk > fghijkabcde
 
# print(S)
idx = 0
for q in query:
    if q[0] == 1:
        idx += q[1]
        if idx >= slen:
            idx -= slen
    else:
#         if q[1]-idx-1 > slen:
#             print(S[q[1]-idx-1-slen], idx)
#         else:
#             print(S[q[1]-idx-1], idx)
        print(S[q[1]-idx-1])