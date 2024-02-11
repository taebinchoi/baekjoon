N = int(input())

for i in range(5*N):
    if i < N:
        for j in range(5*N):
            print("@", end='')
    if i >= 4*N:
        for j in range(5*N):
            print("@", end='')
    if N <= i < 4*N:
        for j in range(N):
            print("@", end='')
    print()