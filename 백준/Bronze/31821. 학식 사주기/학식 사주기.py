N = int(input())
K = [int(input()) for i in range(N)]
res = 0

M = int(input())
for j in range(M):
    L = int(input())
    res += K[L-1]

print(res)