Y1, M1, D1 = map(int, input().split())
Y2, M2, D2 = map(int, input().split())

if M2 > M1 or (M1 == M2 and D1 <= D2):
    print(Y2 - Y1)
else:
    print(Y2 - 1 - Y1)
print(Y2 + 1 - Y1)
print(Y2 - Y1)