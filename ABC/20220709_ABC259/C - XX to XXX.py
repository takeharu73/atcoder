##### 2WA。原因が分からず死亡。
##### ランレングス圧縮を先に気付くべきだった。


S = input()
T = input()
# a,b,d = list(map(int,input().split()))
# query = [list(map(int,input().split())) for _ in range(Q)]
i = 0
j = 0
prev_s = ""
prev_t = ""
cont_f = 0
flg = 0
while True:
    if i<len(S) and j<len(T):
        if S[i] == T[j]:
            if S[i] == prev_s and T[j] == prev_t:
                cont_f = 1
            else:
                cont_f = 0
            prev_s = S[i]
            prev_t = T[j]
            i += 1
            j += 1
        else:
            if prev_s == "":
                print("No")
                flg = 1
                break
            else:
                if S[i]==prev_s and cont_f == 1:
                    prev_s = S[i]
                    i += 1
                elif T[j]==prev_t and cont_f == 1:
                    prev_t = T[j]
                    j += 1
                else:
                    print("No")
                    flg = 1
                    break
    elif i<len(S):
        if S[i] == prev_s and cont_f==1:
            i += 1
        else:
            print("No")
            flg = 1
            break
    elif j<len(T):
        if T[j] == prev_t and cont_f==1:
            j += 1
        else:
            print("No")
            flg = 1
            break
    else:
        break
if flg == 0:
    print("Yes")