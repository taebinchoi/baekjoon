N = input()
M = int(input())
L = N[0:5]
tot = 0
for i in range(M):
    K = input()
    if K[0:5] == L:
        tot += 1

print(tot)