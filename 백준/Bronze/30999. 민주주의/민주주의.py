N, M = map(int,input().split())
tot = 0
for i in range(N):
    K = list(input())
    A = K.count('O')
    B = K.count('X')
    if A > B:
        tot += 1
        
print(tot)