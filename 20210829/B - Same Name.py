N = int(input())
name = {}
flg = 0
for i in range(N):
    if flg == 0:
        S, T = input().split(" ")
        if S not in name.keys():
            name[S] = []
            name[S].append(T)
        else:
            if T in name[S]:
                print("Yes")
                flg = 1
            else:
                name[S].append(T)