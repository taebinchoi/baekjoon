N = int(input())
M = input().split()
K = list(map(int, M))
total = sum(K) + 8*(N-1)

A = total // 24
B = total % 24
print(A, B)