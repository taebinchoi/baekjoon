K, N, M = map(int,input().split())
1 <= K, N <= 1000
1 <= M <= 100000

if K*N == M or K*N < M:
    print(0)
else:
    print(K*N - M)