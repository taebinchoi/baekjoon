N = int(input())
M = 2

while True:
    if (N == 1 or N == 2):
        print(N)
        break
    M *= 2
    if M >= N:
        print((N-(M//2))*2)
        break