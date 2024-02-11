import sys
input = sys.stdin.readline
N = int(input())
D, P = 0, 0

for i in range(N):
    M = input().rstrip()
    if M == 'D':
        D += 1
    else:
        P += 1
    if abs(D-P)>1:
        print(f"{D}:{P}")
        break
else:
    print(f"{D}:{P}")