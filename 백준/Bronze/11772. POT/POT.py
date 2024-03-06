N = int(input())
M = [input() for i in range(N)]
tot = sum([int(j[:-1])**int(j[-1]) for j in M])

print(tot)