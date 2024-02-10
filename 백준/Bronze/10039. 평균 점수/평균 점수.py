S = 0
for i in range(5):
    A = int(input())
    if A < 40:
        S += 40
    else:
        S += A
print(int(S / 5))