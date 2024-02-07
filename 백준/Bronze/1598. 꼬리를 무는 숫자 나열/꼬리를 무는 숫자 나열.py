M, N = map(int,input().split())
M -= 1
N -= 1
print(abs(M//4-N//4) + abs(M%4-N%4))