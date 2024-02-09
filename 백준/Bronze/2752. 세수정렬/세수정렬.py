A, B, C = map(int,input().split())
A != B and A != C and B != C

if A > B > C:
    print(C, B, A)
elif A > C > B:
    print(B, C, A)
elif B > A > C:
    print(C, A, B)
elif B > C > A:
    print(A, C, B)
elif C > A > B:
    print(B, A, C)
else:
    print(A, B, C)