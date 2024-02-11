A, B, C = map(int,input().split())
if min(A, B, C) == A:
    print(B+C)
elif min(A, B, C) == B:
    print(A+C)
else:
    print(A+B)