N,M = list(map(int, input().split()))
A = list(map(int, input().split()))[::-1]
C = list(map(int, input().split()))[::-1]
 
len_A = len(A)
len_C = len(C)
len_B = len_C-len_A+1
 
# print(A)
res = []
sum_kei_C = [0]*len_C
# print("len_A", len_A, "len_B", len_B, "len_C", len_C )
 
# iはBの高次元から
for i in range(len_C-len_A+1):
#     kei_B = C[i]/A[i]
    kei_B = (C[i]-sum_kei_C[len_C-i-1])/A[0]
    # jはAの高次元から
    for j in range(len_A):
        # sum_kei_CはCの低次元から
#         print(len_B,len_A, (len_B-i-1)+(len_A-j-1)+1)
        sum_kei_C[(len_B-i-1)+(len_A-j-1)]+= kei_B*A[j]
    res.append(str(int(kei_B)))
#     print(res)
    
# print("結果")
print(" ".join(res[::-1])) 