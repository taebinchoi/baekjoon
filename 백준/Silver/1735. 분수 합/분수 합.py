import math

A, B = map(int, input().split())
C, D = map(int, input().split())

N = math.gcd(A*D + C*B, B*D) 
print((A*D + C*B)//N, B*D//N)