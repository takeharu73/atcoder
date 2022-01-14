def f(x):
    return x**2+x*2+3
 
t = int(input())
print(f(f(f(t)+t)+f(f(t))))