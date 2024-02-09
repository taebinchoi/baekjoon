N = int(input())
A = 0
B = 1

for i in range(N):
    A, B = B, A+B

print(A)