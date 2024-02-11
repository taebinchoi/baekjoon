M, N = 0, 1e9
for i in range(int(input())):
    K, L = map(int, input().split())
    if N > L:
        M, N = K, L
print(M, N)