N = int(input())
tot = 0

for i in range(N):
    M = input()
    if int(M[2:]) <= 90:
        tot += 1
print(tot)