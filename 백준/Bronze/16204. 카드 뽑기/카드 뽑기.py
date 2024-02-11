N, M, K = map(int,input().split())
if M >= K:
    print(N-(M-K))
else:
    print(N-(K-M))