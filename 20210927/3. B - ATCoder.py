S = input()
l = ["A","C","G","T"]
len_max, res = 0, 0
for i, s in enumerate(S):
    if s in l:
        len_max += 1
        if i == len(S)-1 and res < len_max:
            res = len_max
    else:
        if res < len_max:
            res = len_max
        len_max = 0
print(res)