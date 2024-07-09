N = int(input())
M = 0
for i in range(2,N-1,2):
    M += (N-i-2)//2
print(M)
