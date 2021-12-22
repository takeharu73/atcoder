## 以下でAC
n = int(input())

prev1 = 1
prev2 = 1

if n > 1:
    for i in range(n-1):
        next_val = prev1 + prev2
        prev2 = prev1
        prev1 = next_val
else:
    next_val = 1
    
print(next_val)


### 以下はTLE (n=44で3分強)
# n = int(input())

# def fib(n):
#     if n==0 or n==1:
#         return 1
#     return fib(n-1)+fib(n-2)

# print(fib(n))