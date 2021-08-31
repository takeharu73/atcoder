# a+b+c≤S かつ a×b×c≤T を満たす非負整数の組 (a,b,c) はいくつありますか？
 
# 0≤S≤100
# 0≤T≤10000
# S,T は整数である。
S,T = map(int, input().split())
 
result = 0
for i in range(S+1):
    a = i
    for j in range(S-a+1):
        b = j
        for k in range(S-a-b+1):
            c = k
            if a*b*c <= T:
                result += 1
print(result)