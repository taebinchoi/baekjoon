A, B, C, M = map(int,input().split())
N = 0
tot = 0

for i in range(24):
    if N+A <= M:
        N = N+A
        tot += B
    else:
        if N-C >= 0:
            N = N-C
        else:
            N = 0

print(tot)