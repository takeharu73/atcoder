N = int(input())
H = list(map(int, input().split()))

# print(H)

h_prev = H[0]
for i, h in enumerate(H):
    if i==0:
        continue
    elif h>h_prev and i!=len(H)-1:
        h_prev = h
    elif h>h_prev and i==len(H)-1:
        print(h)
        break
    else:
        print(h_prev)
        break
