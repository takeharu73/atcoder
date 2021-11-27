# DFSやDPやダイクストラ法を検討するものの、深く考えすぎで提出できず
# 単純に前からKまで.をつなげた時の長さを計算して最大長をとれば答えだった。。

from collections import deque
 
s = input()
k = int(input())
 
q = deque()
ans = 0
cnt = 0
for c in s:
    q.append(c)
    if c == ".":
        cnt += 1
    while q and cnt > k:
        if q.popleft() == ".":
            cnt -= 1
    ans = max(ans, len(q))
    
print(ans)