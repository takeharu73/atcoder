import sys
N = int(input())
wait = [i+1 for i in range(2*N+1)]
# print(wait)
 
while True:
    print(wait.pop(0))
    sys.stdout.flush()
    if len(wait)==0:
        exit()
        break
    a = int(input())
    wait.remove(a)