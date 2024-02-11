N, M = map(int,input().split())
ball = [0]*N

for p in range(M):
    i, j, k = map(int,input().split())
    for i in range(i, j+1):
        ball[i-1] = k

for i in range(N):
    print(ball[i], end=' ')