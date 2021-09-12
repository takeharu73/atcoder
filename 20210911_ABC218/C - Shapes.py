def rot(S):
    return list(zip(*S[::-1]))
 
def findSameTop(S,T):
    i_s, i_t, j_s, j_t = 0,0,0,0
    flag_S = 0
    flag_T = 0
    for i in range(N):
        for j in range(N):
            if flag_S == 0:
                if S[i][j]=="#":
                    i_s = i
                    j_s = j
                    flag_S = 1            
            if flag_T == 0:
                if T[i][j]=="#":
                    i_t = i
                    j_t = j
                    flag_T = 1
    return([i_t - i_s, j_t - j_s])
 
 
def isSame(S,T):
    flg = 0
    m = findSameTop(S,T)

    for j in range(N):
        for k in range(N):
            if 0<=j+m[0]<N and 0<=k+m[1]<N:
                if S[j][k]!=T[j+m[0]][k+m[1]]:
                    return False
            else:
                if S[j][k]=="#":
                    return False
    return True
 
 
N = int(input())
S = [input() for _ in range(N)]
T = [input() for _ in range(N)]
 
cntS = sum(1 for i in range(N) for j in range(N) if S[i][j]=='#')
cntT = sum(1 for i in range(N) for j in range(N) if T[i][j]=='#')
if cntS != cntT:
    print("No")
    exit()
 
for _ in range(4):
    if isSame(S,T):
        print("Yes")
        exit()
    S = rot(S)
 
print("No")    