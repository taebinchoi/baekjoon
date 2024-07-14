import sys
input = sys.stdin.readline
tot = []

for _ in range(3):
    M, N = map(int, input().split())
    if M*10 >= 5000:
        M = M*10-500
    else:
        M *= 10
    N *= 10
    tot.append(N/M)
    
if max(tot) == tot[0]:
    print('S')
elif max(tot) == tot[1]:
    print('N')
else:
    print('U')