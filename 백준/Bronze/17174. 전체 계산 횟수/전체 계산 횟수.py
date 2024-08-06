N, M = map(int,input().split())
tot = N
while N // M:
    tot += N // M
    N //= M
print(tot)