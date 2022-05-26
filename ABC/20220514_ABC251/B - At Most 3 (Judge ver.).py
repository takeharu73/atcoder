N,W = list(map(int,input().split()))
A = list(map(int,input().split()))
A.insert(0,0)
A.insert(0,0)
# print(A)
w_set = set()
for i in range(N+2):
    for j in range(i+1,N+2):
        for k in range(j+1,N+2):
            sumw = int(A[i] + A[j] + A[k])
#             print(i,j,k,sumw)
            if sumw not in w_set:
                w_set.add(sumw)
 
w_set_l = sorted(list(w_set))
# print(w_set_l)
res = 0
for i in range(len(w_set_l)):
    if w_set_l[i] <= W:
        res += 1
    else:
        break
print(res)