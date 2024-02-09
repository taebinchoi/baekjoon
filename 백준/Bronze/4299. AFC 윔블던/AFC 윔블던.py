M, N = map(int,input().split())
0 <= M and 0 <= N

if M < N:
    print(-1)
else:
    O = (M+N)//2
    P = (M-N)//2
    if (O+P) == M and (O-P) == N:
        print(O, P)
    else:
        print(-1)