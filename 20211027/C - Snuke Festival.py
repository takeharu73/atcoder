N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
 
A = sorted(A)
B = sorted(B)
C = sorted(C)
 
# print(A,B,C)
 
import bisect
res = 0
for i in range(N):
    index_a = bisect.bisect_left(A, B[i])
    a_num = index_a
    index_c = bisect.bisect(C, B[i])
    c_num = N - index_c
#     print(a_num, c_num)
    res += a_num*c_num
print(res)