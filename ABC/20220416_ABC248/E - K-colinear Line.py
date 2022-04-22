N, K= list(map(int, input().split()))
XY = [list(map(int, input().split())) for _ in range(N)]
 
# 全ての点から、ほかの点への傾きを辞書形式で保存する
dic_kata = {}
# 複数の点を起点とする場合全てについて1加算されてしまうので、
seen = []
for i in range(N):
    dic_kata[i] = {}
 
    # すでに前の点を起点として探索済の傾きを登録する
    flg = set()
    for j in range(N):
        if i<j:
            if XY[j][0]-XY[i][0]==0:
                kata = 9999454599999
            else:
                kata = (XY[j][1]-XY[i][1])/(XY[j][0]-XY[i][0])
                if kata==0:
                    kata = 0
            if kata not in flg:
                if dic_kata[i].get(kata):
                    dic_kata[i][kata]+=1
                else:
                    dic_kata[i][kata]=2
        elif i>j:
            if XY[j][0]-XY[i][0]==0:
                kata = 9999454599999
            else:
                kata = (XY[j][1]-XY[i][1])/(XY[j][0]-XY[i][0])
                if kata==0:
                    kata = 0
            if dic_kata[i].get(kata):
                print("del", i, kata)
                del dic_kata[i][kata]
            flg.add(kata)
 
if K == 1:
    print("Infinity")
else:
#     print(dic_kata)
    res = 0
    for i in range(N):
        for k in dic_kata[i].keys():
            if dic_kata[i][k] >= K:
                res += 1
    print(res)