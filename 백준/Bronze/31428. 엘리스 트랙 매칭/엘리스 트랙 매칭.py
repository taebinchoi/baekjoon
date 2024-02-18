N = int(input())
M = list(input().split())
K = input()
tot = 0
for i in M:
    if i == K:
        tot += 1
print(tot)