N = int(input())
S = [list(input()) for _ in range(N)]
 
S_2 = list([list(s) for s in zip(*S)])
 
S_3 = []
s_x = 0
s_y = len(S)-1
 
for i in range(len(S)*2):
    s_3 = []
    x = s_x
    y = s_y
    while True:
        if 0 <= x <= len(S)-1 and 0 <= y <= len(S)-1:
            s_3.append(S[y][x])
            x += 1
            y += 1
        else:
            break
    S_3.append(s_3)
    if s_y > 0:
        s_y -= 1
    elif s_x<len(S)-1:
        s_x += 1
    else:
        break
 
S_4 = []
s_x = 0
s_y = 0
 
for i in range(len(S)*2):
    s_4 = []
    x = s_x
    y = s_y
    while True:
        if 0 <= x <= len(S)-1 and 0 <= y <= len(S)-1:
            s_4.append(S[x][y])
            x -= 1
            y += 1
        else:
            break
    S_4.append(s_4)
    if s_x < len(S)-1:
        s_x += 1
    elif s_y<len(S)-1:
        s_y += 1
    else:
        break
        
# print(S)
# print()
# print(S_2)
# print()
# print(S_3)
# print()
# print(S_4)
 
 
flg = 0
def check(S, flg):
    for i, s in enumerate(S):
        if flg == 1:
            break
        cnt = s.count('#')
        if cnt < 4:
            continue
        else:
            res = 0
            cnt_dot = 0
            cont = 0
            for i, ss in enumerate(s):
 
                if ss == "#":
                    res += 1
                    cont += 1
#            #.##...#..
                else:
                    if cnt_dot==0:
                        res += 1
                        cnt_dot += 1
                        first = cont
                    elif cnt_dot==1:
                        res += 1
                        cnt_dot += 1
                        second = cont
                    elif cnt_dot==2:
#                         cnt_dot -= 1
                        res -= first
                        first = second
                        second = cont
                    cont = 0                    
#                 print(i,ss,res,cont,cnt_dot)
                if res == 6:
                    print("Yes")
                    flg = 1
                    return flg
 
    return flg
 
flg = check(S, flg)
if flg == 0:
    flg = check(S_2, flg)
if flg == 0:
    flg = check(S_3, flg)
if flg == 0:
    flg = check(S_4, flg)
 
if flg == 0:
    print("No")