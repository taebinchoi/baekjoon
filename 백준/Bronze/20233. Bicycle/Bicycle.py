A = int(input())
X = int(input())
B = int(input())
Y = int(input())

T = int(input())

M = A + max(T-30, 0)*X*21
N = B + max(T-45, 0)*Y*21
print(M, N)