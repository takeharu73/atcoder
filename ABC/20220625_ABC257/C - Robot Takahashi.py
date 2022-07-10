N = int(input())
S = list(map(int,list(input())))
W = list(map(int,input().split()))
 
# print(S)
 
child = []
adult = []
 
for i in range(N):
    if S[i] == 0:
        child.append(W[i])
    else:
        adult.append(W[i])
 
child = sorted(child)        
adult = sorted(adult)
# print(child)
# print(adult)
num_child = len(child)
num_adult = len(adult)
flg = 0
 
if num_child == 0 or num_adult == 0:
    print(N)
    flg = 1
 
import bisect
 
if flg == 0:
    if child[-1]<adult[0]:
        print(N)
    else:
        res = 0
        # adultの値を1つずつ閾値として、最大の結果を探る
        for i in range(num_adult):
            if child[0]<=adult[i]-1<=child[-1]:
                idx = bisect.bisect(child, adult[i]-1)
            elif adult[i]-1<child[-1]:
                idx = 0
            else:
                idx = num_child
#             print(adult[i], idx, num_adult-i, num_adult-i+idx, idx)
            if res < num_adult-i+idx:
                res = num_adult-i+idx
            
        print(res)