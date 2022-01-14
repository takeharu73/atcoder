# コンテスト中はTLE。heapqに気づけず。
# 最小値or最大値の取り出し・挿入を高速でやるならheapq

import heapq
N,K = map(int,input().split())
P = list(map(int,input().split()))
que = P[0:K]
print(min(que))
# heapqに変換
heapq.heapify(que)
for i in range(K,N):
    # 最小値を求める O(logN)
    minima = heapq.heappop(que)
    # 現最小値かP[i]の小さいほうは捨てる
    minima = max(minima,P[i])
    # 要素を挿入 O(logN)
    heapq.heappush(que,minima)
    # 最小値を求める O(logN)
    ans = heapq.heappop(que)
    print(ans)
    # 要素を挿入 O(logN)
    heapq.heappush(que,ans)