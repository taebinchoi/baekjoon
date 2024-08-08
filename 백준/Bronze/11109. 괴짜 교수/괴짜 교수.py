T = int(input())
for i in range(T):
    D, N, S, P = map(int, input().split())
    if D + P*N == N*S:
        print("does not matter")
    elif D + P*N > N*S:
        print("do not parallelize")
    else:
        print("parallelize")