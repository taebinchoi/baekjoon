from math import factorial
N, K = list(map(int, input().split()))

A = (factorial(N) // (factorial(K) * factorial(N-K)))
B = A%10007
print(B)