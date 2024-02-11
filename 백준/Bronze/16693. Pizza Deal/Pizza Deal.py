from math import pi

A1, P1 = map(int,input().split())
R1, P2 = map(int,input().split())
if max(A1/P1, (R1*R1*pi)/P2) == A1/P1:
    print('Slice of pizza')
else:
    print('Whole pizza')