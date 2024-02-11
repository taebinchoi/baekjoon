N = int(input())
M = list(map(int,input().split()))
tot = 0

for i in range(1, N+1):
    if M[i-1] != i:
        tot += 1

print(tot)