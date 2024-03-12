N = int(input())
M = list(map(int, input().split()))
tot, K = 0, 1

for N in M:
    if N != K:
        tot += 1
    else:
        K += 1
print(tot)