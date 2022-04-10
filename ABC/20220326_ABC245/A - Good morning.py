A, B, C, D = list(map(int, input().split()))
 
if A<C:
    print("Takahashi")
elif A==C:
    if B<=D:
        print("Takahashi")
    else:
        print("Aoki")
else:
    print("Aoki")