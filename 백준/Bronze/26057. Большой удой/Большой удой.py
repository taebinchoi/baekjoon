L = int(input())
T = int(input())

A = max(L-T, T)
B = min(L-T, T)
print(A-B)