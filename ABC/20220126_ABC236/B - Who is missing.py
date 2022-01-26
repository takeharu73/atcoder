N = int(input())
A = list(map(int,input().split()))

dic = {}
for a in A:
    if dic.get(a) is None:
        dic[a]=1
    else:
        dic[a]+=1

for d in dic.keys():
    if dic[d]==3:
        print(d)