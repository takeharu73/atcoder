N, K = list(map(int, input().split()))
# P = [list(map(int, input().split())) for _ in range(N)]
P_sum = [0]*N

for i in range(N):
    P = list(map(int, input().split()))
    P_sum[i] = sum(P)

# print(P_sum)

P_sum_sorted = sorted(P_sum, reverse=True)
T = P_sum_sorted[K-1]
# print(P_sum_sorted, T)

for i in range(N):
    if T - P_sum[i] <= 300:
        print("Yes")
    else:
        print("No")
