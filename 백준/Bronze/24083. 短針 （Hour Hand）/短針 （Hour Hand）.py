A = int(input())
B = int(input())
C = A+B
if C%12 == 0:
    print(12)
else:
    print(int(C%12))