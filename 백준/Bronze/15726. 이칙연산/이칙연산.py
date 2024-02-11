A, B, C = map(int,input().split())
A < B < C

D = int(A*B/C)
E = int(A/B*C)

print(max(D, E))