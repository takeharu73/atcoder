S = input()
lens = len(S)
 
if 6%lens != 0:
    print((6//lens)*S + S[:6%lens])
else:
    print((6//lens)*S)