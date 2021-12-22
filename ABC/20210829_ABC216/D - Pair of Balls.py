def has_duplicates(seq):
    return len(seq) != len(set(seq))
 
N, M = map(int, input().split(" "))
flg = 0
 
dic_up={}
dic_down={}
for i in range(M):
    if flg == 0:
        k = int(input())
        A = list(map(int,input().split(" ")))
        if has_duplicates(A):
            print("No")
            flg = 1
            break
        for j in range(k):
            if flg == 0:
                if A[j] not in dic_up.keys():
                    # その要素の上の要素をすべて格納
                    dic_up[A[j]]=A[:j]
                    # その要素の下の要素をすべて格納
                    dic_down[A[j]]=A[j+1:]
                else:
                    if flg == 0:
                        for e in A[:j]:
                            if e in dic_down[A[j]]:
                                print("No")
                                flg = 1
                                break
                    if flg == 0:
                        for e in A[j+1:]:
                            if e in dic_up[A[j]]:
                                print("No")
                                flg = 1
                                break
if flg==0:
    print("Yes")