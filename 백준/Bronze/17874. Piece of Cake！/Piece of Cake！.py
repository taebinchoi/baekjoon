N, H, V = map(int,input().split())
A = max(N-H, H)
B = max(N-V, V)
print(A*B*4)