N, M = map(int,input().split())
if -1 <= (max(N, M)-min(N, M)) <= 1:
    print(N+M)
else:
    print(2*min(N, M)+1)