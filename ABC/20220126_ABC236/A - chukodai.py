S = list(input())
a,b = list(map(int,input().split()))

tmp = S[a-1]
S[a-1] = S[b-1]
S[b-1] = tmp

print("".join(S))