N, H = map(int,input().split())
M = list(map(int,input().split()))
K = len(M)
tot = 0

for i in range(K):
    if M[i] <= H:
        tot += 1
print(tot)