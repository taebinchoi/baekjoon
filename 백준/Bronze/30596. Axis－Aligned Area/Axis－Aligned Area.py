A1 = int(input())
A2 = int(input())
A3 = int(input())
A4 = int(input())

if A1 == A2 == A3 == A4:
    print(A1*A2)
if A1 == A2 == A3 < A4:
    print(A1*A2)
if A1 == A2 < A3 == A4:
    print(A2*A3)
if A1 < A2 == A3 == A4:
    print(A1*A2)
if A1 == A2 < A3 < A4:
    print(A2*A3)
if A1 < A2 == A3 < A4:
    print(A1*A2)
if A1 < A2 < A3 == A4:
    print(A1*A3)
if A1 < A2 < A3 < A4:
    print(A1*A3)