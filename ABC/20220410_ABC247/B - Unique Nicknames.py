N = int(input())
ST = [list(input().split()) for _ in range(N)]
 
# print(ST)
 
seen = {}
flg = 0
for s,t in ST:
    if s != t:
        if seen.get(s) is None:
            seen[s] = 1
        else:
            seen[s] += 1
        if seen.get(t) is None:
            seen[t] = 1
        else:
            seen[t] += 1
    else:
        if seen.get(s) is None:
            seen[s] = 1
        else:
            seen[s] += 1
    
for s,t in ST:
    if seen[s]>=2 and seen[t]>=2:
        print("No")
        flg = 1
        break
        
if flg == 0:
    print("Yes")