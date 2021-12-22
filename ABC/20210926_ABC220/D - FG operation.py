%%time
import collections

IN = iter(Input.split('\n')).__next__
def input():
    return IN()

N = int(input())
#make a deque from your list
A = collections.deque(list(map(int, input().split())))

MOD = 998244353

def cal(dp, X):
    dp_up = [0]*10
    for i in range(10):
#         dp_up[(i*X)%10] += dp[i]
#         dp_up[(i+X)%10] += dp[i]
        dp_up[(i*X)%10] = (dp_up[(i*X)%10] + dp[i])%MOD
        dp_up[(i+X)%10] = (dp_up[(i+X)%10] + dp[i])%MOD
    return dp_up

dp = []
dp.append([0]*10)
# print(d)
dp[0][A[0]]=1
A.popleft()

X = A[0]
for i in range(N):
    dp.append(cal(dp[i], X))
    A.popleft()
    if i == N-2:
        break
    else:
        X = A[0]

res = dp[-1]        
for r in res:
    print(r)