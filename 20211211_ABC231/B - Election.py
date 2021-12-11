import collections
 
N = int(input())
S = []
for i in range(N):
    S.append(input())
S_num = collections.Counter(S)
S_num = sorted(S_num.items(), key=lambda x:x[1], reverse=True)
print(S_num[0][0])