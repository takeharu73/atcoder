Q = int(input())
query = [list(map(int, list(input().split()))) for _ in range(Q)]
 
# print(query)
 
dic = {}
idx_in = 0
idx_out = 0
for q in query:
    if q[0] == 1:
        dic[idx_in] = [q[1], q[2], q[1]*q[2]]
        idx_in += 1
    else:
        res = 0
        numball = q[1]
#         print(dic)
        while True:
            if numball == 0:
                print(res)
                break
            elif numball >= dic[idx_out][1]:
                res += dic[idx_out][2]
                numball -= dic[idx_out][1]
                idx_out += 1
            else:
#                 print(dic[idx_out], numball)
                res += dic[idx_out][0]*numball
                dic[idx_out][1] -= numball
                dic[idx_out][2] -= dic[idx_out][0]*numball
                print(res)
                break