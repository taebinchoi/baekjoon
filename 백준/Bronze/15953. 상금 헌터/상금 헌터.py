import sys
input = sys.stdin.readline
N = int(input())
for i in range(N):
    M, K = map(int, input().split())
    tot = 0

    if M == 0:
        pass
    elif M <= 1:
        tot += 500
    elif M <= 3:
        tot += 300
    elif M <= 6:
        tot += 200
    elif M <= 10:
        tot += 50
    elif M <= 15:
        tot += 30
    elif M <= 21:
        tot += 10

    if K == 0:
        pass
    elif K <= 1:
        tot += 512
    elif K <= 3:
        tot += 256
    elif K <= 7:
        tot += 128
    elif K <= 15:
        tot += 64
    elif K <= 31:
        tot += 32
    print(tot*10000)