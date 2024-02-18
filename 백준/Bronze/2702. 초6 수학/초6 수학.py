import math
T = int(input())
for i in range(T):
    M, N = map(int,input().split())
    A = math.lcm(M, N)
    B = math.gcd(M, N)
    print(A, B)