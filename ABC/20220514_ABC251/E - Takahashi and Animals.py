N = int(input())
A = list(map(int,input().split()))
 
# i番目の動物まで餌あげるのにかかる最小金額DP
DP = [0]*N
 
# 最初に1番目・２番目の動物にエサをあげる場合
DP[0] = A[0]
DP[1] = A[0]
 
for i in range(2,N):
    DP[i] = min(DP[i-2]+A[i-1], DP[i-1]+A[i])
 
# print(DP)
# print(len(DP))
 
DP_2 = [0]*N
 
# 最初にN番目・1番目の動物にエサをあげる場合
DP_2[0] = A[-1]
DP_2[1] = A[-1]+A[1]
for i in range(2,N-1):
    DP_2[i] = min(DP_2[i-2]+A[i-1], DP_2[i-1]+A[i])
 
# print(DP_2)
# print(len(DP_2))
 
print(min(DP[-1], DP_2[-2],))