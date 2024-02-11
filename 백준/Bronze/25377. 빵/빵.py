A = 999999999
B = A
N = int(input())
for i in range(N):
    M, K = map(int,input().split())
    if M <= K:
        B = min(B, K)
if B == A:
    print(-1)
else:
    print(B)