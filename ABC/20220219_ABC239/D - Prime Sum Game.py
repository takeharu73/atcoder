sosuu = set([2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199])

flg = 0
A, B, C, D = list(map(int, input().split()))

flg_takahashi = 0
for t in range(A, B+1):
    flg = 0
    for a in range(C, D+1):
        if t+a in sosuu:
            flg = 1
            break
    if flg == 0:
        print("Takahashi")
        flg_takahashi = 1
        break
if flg_takahashi==0:
    print("Aoki")