N, X = list(map(int, input().split()))
L = []
A = []
for i in range(N):
    a = list(map(int, input().split()))
    L.append(a[0])
    A.append(a[1:])
 
def f(x, remain, res):
    """
    xを残りの袋の中から1つずつ選ぶボールで構成する組み合わせの数を返す
    """
    if len(remain) == 1:
        res_last = 0
        for r in remain[0]:
            if x == r:
                res_last += 1
        return res_last
    else:
        res_each = 0
        for r in remain[0]:
            if x%r == 0:
                res_each += f(x//r, remain[1:], res)
    return res + res_each
 
print(f(X, A, 0))