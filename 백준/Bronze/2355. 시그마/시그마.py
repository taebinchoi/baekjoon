N, M = map(int, input().split())
MX = max(N, M)
MN = min(M, N)
K = MX - MN

sum = (K*(K+1))//2
print(sum+MN*(K+1))