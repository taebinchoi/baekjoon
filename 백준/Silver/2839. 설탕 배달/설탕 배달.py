N = int(input())
A = 0
B = 0
while True:
    if N % 5 == 0:
        B = N // 5
        print(A + B)
        break
    N -= 3
    A += 1
    if N < 0:
        print(-1)
        break