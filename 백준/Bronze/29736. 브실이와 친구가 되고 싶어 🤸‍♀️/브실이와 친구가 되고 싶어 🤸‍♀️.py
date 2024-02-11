A, B = map(int,input().split())
K, X = map(int,input().split())
tot = 0

for i in range(K-X, K+X+1):
    if A <= i <= B:
        tot += 1
        
if tot == 0:
    print('IMPOSSIBLE')
else:
    print(tot)