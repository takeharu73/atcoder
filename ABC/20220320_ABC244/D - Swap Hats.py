S = "".join(input().split())
T = "".join(input().split())
 
if T==S or T=="".join(S[1:])+S[0] or T==S[2]+"".join(S[:2]):
    print("Yes")
else:
    print("No")