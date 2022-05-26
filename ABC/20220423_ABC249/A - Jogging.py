A, B,C, D,E,F,X= list(map(int, input().split()))
 
a_dis = X//(A+C) * A*B + min(X%(A+C), A)*B
d_dis = X//(D+F) * D*E + min(X%(D+F), D)*E
 
if a_dis>d_dis:
    print("Takahashi")
elif a_dis<d_dis:
    print("Aoki")
else:
    print("Draw")