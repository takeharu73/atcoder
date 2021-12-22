N,M = list(map(int, input().split()))
A = list([list(input()) for _ in range(2*N)])
 
res = [i for i in range(2*N)]
score = {i:0 for i in range(2*N)}
 
# i にi番目の順位の人を入れる
for j in range(M):
    for i in range(0,2*N,2):
        if (A[res[i]][j]=="G" and A[res[i+1]][j]=="P") or (A[res[i]][j]=="P" and A[res[i+1]][j]=="C") or (A[res[i]][j]=="C" and A[res[i+1]][j]=="G"):
            score[res[i+1]] += 1
        elif (A[res[i]][j]=="P" and A[res[i+1]][j]=="G") or (A[res[i]][j]=="C" and A[res[i+1]][j]=="P") or (A[res[i]][j]=="G" and A[res[i+1]][j]=="C"):
            score[res[i]] += 1
        res = [k for k, _ in sorted(score.items(), key=lambda x:x[1], reverse=True)]
 
for i in range(2*N):
    print(res[i]+1)