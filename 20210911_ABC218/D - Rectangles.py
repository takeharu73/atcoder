N = int(input())
X, Y = [],[]
dic = {}
for i in range(N):
    x,y = input().split()
    if dic.get(x):
        dic[x].append(y)
    else:
        dic[x]=[y]   
 
 
import itertools
from collections import defaultdict
list_dic = {}
result = 0
 
for i in dic.keys():
    # 以下のsortを追加してAC
    dic[i].sort()
    for j in list(itertools.combinations(dic[i], r=2)):
        if list_dic.get(j):
            list_dic[j] += 1
        else:
            list_dic[j] = 1
 
 
from operator import mul
from functools import reduce
 
 
for v in list_dic.values():
    result += v*(v-1)//2
print(result)