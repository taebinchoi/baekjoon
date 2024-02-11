N = int(input())
M = list(map(int,input().split()))
K = list(map(int,input().split()))
rust = 0

for i in range(N):
    if M[i] <= K[i]:
        rust += 1
print(rust)