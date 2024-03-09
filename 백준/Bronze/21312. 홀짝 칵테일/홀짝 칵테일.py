A, B, C = map(int,input().split())
if A%2 == 0 and B%2 == 0 and C%2 == 0:
    print(A*B*C)
elif A%2 == 1 and B%2 == 0 and C%2 == 0:
    print(A)
elif A%2 == 0 and B%2 == 1 and C%2 == 0:
    print(B)
elif A%2 == 0 and B%2 == 0 and C%2 == 1:
    print(C)
elif A%2 == 1 and B%2 == 1 and C%2 == 0:
    print(A*B)
elif A%2 == 1 and B%2 == 0 and C%2 == 1:
    print(A*C)
elif A%2 == 0 and B%2 == 1 and C%2 == 1:
    print(B*C)
else:
    print(A*B*C)