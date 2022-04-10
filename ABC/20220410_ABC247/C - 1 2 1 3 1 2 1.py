N = int(input())
 
def f(x):
    if x >= 2:
        return f(x-1) + " " + str(x) + " " + f(x-1)
    else:
        return str(x)
 
print(" ".join(f(N).split(" ")))