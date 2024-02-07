N = int(input())
A, B, C = 1, 0, 0
for i in range(1, N+1):
    A *= i
B = A
while B%10 == 0:
    B = B//10
    C += 1
    
print(C)