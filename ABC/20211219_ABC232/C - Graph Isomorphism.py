N,M = list(map(int, input().split()))
AB = [list(map(int, input().split())) for _ in range(M)]
CD = [list(map(int, input().split())) for _ in range(M)]
 
import itertools
flg=0
l = [i+1 for i in range(N)]
 
def compare(AB, CD, P):
    dic_ab = {}
    dic_cd = {}
    dic = {}
    for ab in AB:
        if dic_ab.get(ab[0]) is None:
            dic_ab[ab[0]] = [ab[1]]
        else:
            dic_ab[ab[0]].append(ab[1])
        if dic_ab.get(ab[1]) is None:
            dic_ab[ab[1]] = [ab[0]]
        else:
            dic_ab[ab[1]].append(ab[0])
    for cd in CD:
        if dic_cd.get(cd[0]) is None:
            dic_cd[cd[0]] = [cd[1]]
        else:
            dic_cd[cd[0]].append(cd[1])
        if dic_cd.get(cd[1]) is None:
            dic_cd[cd[1]] = [cd[0]]
        else:
            dic_cd[cd[1]].append(cd[0])
            
    for i in range(len(P)):
        dic[i+1] = P[i]

    for d in dic_ab.keys():
        dic_ab[d] = sorted(dic_ab[d])
    
    dic_cd_up = {}
    for d,e in dic_cd.items():
        if dic_cd_up.get(dic[d]) is None:
            dic_cd_up[dic[d]] = sorted([dic[a] for a in e])
    return dic_cd_up == dic_ab
    
for P in itertools.permutations(l, N):
    if compare(AB,CD,P):
        print("Yes")
        flg = 1
        break
if flg==0:
    print("No")