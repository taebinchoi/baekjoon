import math

A, B, C = map(int,input().split())
if A == 0:
    A = C**2-B
    print(A)
if B == 0:
    B = C**2-A
    print(B)
if C == 0:
    C = int(math.sqrt(A+B))
    print(C)