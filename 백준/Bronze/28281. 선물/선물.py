N, X = map(int, input().split())
M = list(map(int, input().split()))
tot = []

for i in range(N-1):
    tot.append((M[i] + M[i+1])*X)

print(min(tot))