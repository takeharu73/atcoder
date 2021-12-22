import itertools
S, K = input().split()
K = int(K)
 
S_l = list(S)
S_l_a = list(itertools.permutations(S_l, len(S_l)))
A = sorted(set(S_l_a))
print("".join(A[K-1]))