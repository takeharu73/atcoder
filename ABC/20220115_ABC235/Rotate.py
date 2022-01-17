abc = list(input())
bca = int("".join([abc[1], abc[2], abc[0]]))
cab = int("".join([abc[2], abc[0], abc[1]]))
abc = int("".join(abc))

print(abc+bca+cab)
