N = int(input())
tot = 0

for i in range(1, N+1):
    M = list(map(int, str(i)))
    tot = sum(M) + i
    if tot == N:
        print(i)
        break
    if i == N:
        print(0)