H,W = list(map(int,input().split()))
R,C = list(map(int,input().split()))
 
 
if H==1 and W==1:
    print(0)
elif H==1:
    if W==C or C==1:
        print(1)
    else:
        print(2)
elif W==1:
    if R==H or R==1:
        print(1)
    else:
        print(2)    
elif (R==H or R==1) and (W==C or C==1):
    print(2)
elif (R==H or R==1) or (W==C or C==1):
    print(3)
else:
    print(4)