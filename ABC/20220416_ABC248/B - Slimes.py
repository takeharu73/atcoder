A, B, K = list(map(int, list(input().split())))
res = 0
while True:
    if A >= B:
        break
    else:
        res += 1
        A *= K
print(res)