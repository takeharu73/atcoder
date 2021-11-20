IN = iter(Input.split('\n')).__next__
def input():
    return IN()

Q = int(input())
TX = []
N = 2**20
# print(N)
for i in range(Q):
    TX.append(list(map(int, input().split())))
# print(TX)
 
A = [-1]*N
 
# 既知のindexを格納するseenを用意し、-1が連続する場合はいくつスキップしてよいかを判定する
# 上を導入するも、addtional test caseでTLE。
seen = {}
for tx in TX:
    if tx[0] == 1:
        first_index = tx[1]%N
        index = tx[1]%N
        if seen.get(index) is None:
            seen[first_index] = 0
        while True:
            seen[first_index] += 1
            if seen.get(index) is not None:
                index += (seen[index]-1)
            if A[index] == -1:
                A[index] = tx[1]
                break
            else:
                
                index += 1
                if index >= N:
                    index = 0
    else:
        print(A[tx[1]%N])