A = int(input())
B = int(input())
C = int(input())
A > 0 and A < 180
B > 0 and B < 180
C > 0 and C < 180

if A + B + C == 180:
    if A == B != C or A == C != B or B == C != A:
        print("Isosceles")
    if A != B and B != C and C != A:
        print("Scalene")
    if A == B == C:
        print("Equilateral")
else:
    print("Error")