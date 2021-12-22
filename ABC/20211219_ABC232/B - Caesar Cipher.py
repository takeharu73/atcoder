S = input()
T = input()
 
dif = int(S[0], 36) - int(T[0], 36)
# print(dif)
flg = 0
for i in range(len(S)):
    d = int(S[i], 36) - int(T[i], 36)
#     print(d)
    if d != dif and d+26!=dif and d-26!=dif:
        print("No")
        flg = 1
        break
if flg == 0:
    print("Yes")