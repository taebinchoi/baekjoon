L, R, A = map(int, input().split())
M, N = min(L, R), max(L, R)
K = min(A, N-M)
M += K
A -= K

tot = M*2 + (A//2*2 if A else 0)
print(tot)