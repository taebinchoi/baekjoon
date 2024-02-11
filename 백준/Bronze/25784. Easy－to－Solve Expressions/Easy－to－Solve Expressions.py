A, B, C = map(int,input().split())
if A + B == C or A + C == B or B + C == A:
    print(1)
elif A*B == C or A*C == B or B*C == A:
    print(2)
else:
    print(3)