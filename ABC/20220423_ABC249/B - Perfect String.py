S= input()
 
flg_s = 0
flg_l = 0
flg_seen = 0
seen = set()
 
for s in S:
    if s.islower():
        flg_s = 1
    else:
        flg_l = 1
    if s in seen:
        flg_seen = 1
    else:
        seen.add(s)
if flg_l==1 and flg_s==1 and flg_seen == 0:
    print("Yes")
else:
    print("No")