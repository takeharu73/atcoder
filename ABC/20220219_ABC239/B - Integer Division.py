x = input()

if int(x)//10 == 0:
    print(0)
elif int(x)//10 == -1:
    print(-1)
elif int(x)%10 == 0:
    print(int(x[:-1]))
elif int(x)<0:
    print(int(x[:-1])-1)
else:
    print(int(x[:-1]))