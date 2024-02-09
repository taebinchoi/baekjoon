A, B = map(int,input().split())

C = A//100
D = (A-100*C)//10
E = A-100*C-10*D
F = B//100
G = (B-100*F)//10
H = B-100*F-10*G
I = 100*E+10*D+C
J = 100*H+10*G+F

if I > J:
    print(I)
else:
    print(J)