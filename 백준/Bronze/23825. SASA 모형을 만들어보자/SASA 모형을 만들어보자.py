N, M = map(int,input().split())
if N == M:
    print(N//2)
else:
    print(((min(N, M))//2))