# kの範囲が絞られる点に気づき何とかAC。実装に時間がかかった。

N,A,B = list(map(int, input().split()))
P,Q,R,S = list(map(int, input().split()))
 
k1 = max(1-A,1-B)
k1 = max(k1,max(P-A-1,R-B-1))
 
k2 = min(N-A,N-B)
k2 = min(k2,min(Q-A+1, S-B+1))
 
# k1～k2のうちP-AかつR-B～Q-AかつS-Bに収まる部分だけ見たい 

black = set()
 
 
for k in range(k1,k2+1):
    black.add(str(A+k)+"-"+str(B+k))
 
k3 = max(1-A,B-N)
k3 = max(k3,max(P-A-1, B-S-1))
 
k4 = min(N-A,B-1)
k4 = min(k4,min(Q-A+1, B-R+1))

# k3～k4のうちP-AかつB-S～Q-AかつB-Rに収まる部分だけ見たい

for k in range(k3,k4+1):
    black.add(str(A+k)+"-"+str(B-k))
 
for i in range(P, Q+1):
    row = []
    for j in range(R, S+1):
        if str(i)+"-"+str(j) in black:
            row.append("#")
        else:
            row.append(".")
    print("".join(row))