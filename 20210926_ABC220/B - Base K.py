IN = iter(Input.split('\n')).__next__
def input():
    return IN()

K = int(input())
A, B = input().split()

A_K = int(A,K)
B_K = int(B,K)

print(A_K * B_K)