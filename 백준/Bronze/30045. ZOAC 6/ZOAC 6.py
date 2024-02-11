N = int(input())
oioi = 0
for i in range(N):
    M = input()
    if ('01' in M) or ('OI' in M):
        oioi += 1

print(oioi)