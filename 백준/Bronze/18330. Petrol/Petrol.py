N = int(input())
K = int(input())
A = min(K+60, N)
tot = A*1500 + (N-A)*3000

print(tot)