from functools import lru_cache
# メモ化再帰の方法が分からずWA
# 便利なデコレータ→@lru_cache
# @lru_cacheは、同じ返り値を返すことはできても、実際には処理が実行されないので、関数の中でglobal変数resを更新するなどの処理は不可。
# もし同じことをデコレータ使わずにやる場合→https://qiita.com/chi-na/items/b903bd7cd7433e3a8a3f

x = int(input())
mod = 998244353

res = 1
dic = {}
dic_res = {}

@lru_cache()
def f(x):
    """、
    xあるいは⌊2/x⌋*⌈2/x⌉の、いずれか大きい方を返す
    """
    global res
    
    if x>4:
        return f((x+1)//2) * f(x//2) % mod
    else:
        return x

print(f(x))

# 自分のやろうとしていたこと

# def f(x):
#     dic[x]=1
#     if x>4:
#         if x%2==0:
#             f(x//2)
#             f(x//2)
#         else:
#             f(x//2)
#             f(x//2+1)
#     else:
#         res *= x
#         if res > mod:
#             res = res%mod
# f(x)
# print(dic)
