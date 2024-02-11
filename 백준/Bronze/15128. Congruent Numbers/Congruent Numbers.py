P1, Q1, P2, Q2 = map(int, input().split())

R = P1/Q1 * P2/Q2/2
if int(R) == R:
    print(1)
else:
    print(0)