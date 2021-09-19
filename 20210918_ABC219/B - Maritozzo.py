S1 = input()
S2 = input()
S3 = input()
T = map(int, list(input()))
 
res = ""
for t in T:
    if t==1:
        res+=S1
    elif t==2:
        res+=S2
    elif t==3:
        res+=S3
 
print(res)