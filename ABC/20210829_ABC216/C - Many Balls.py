N = int(input())
result=[]
while True:
    if N > 0:
        if N%2 == 0:
            N = N//2
            result.append("B")
        else:
            N = N-1
            result.append("A")
    else:
        break
print("".join(result[::-1]))