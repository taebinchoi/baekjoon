for _ in range(int(input())):
    M, N = map(int,input().split())
    print(M//N + (1 if M%N else 0))