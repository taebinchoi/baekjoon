C, K, P = map(int,input().split())
M = 0
for i in range(1, C+1):
    M+= K*i + P*(i**2)
print(M)