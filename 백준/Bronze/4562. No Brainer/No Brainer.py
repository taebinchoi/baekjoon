N = int(input())

for i in range(N):
    N, M = map(int,input().split())

    if N < M:
        print("NO BRAINS")
    else:
        print("MMM BRAINS")