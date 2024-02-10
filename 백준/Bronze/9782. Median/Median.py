T = 0
while True:
    M = [*map(int, input().split())]
    if M[0] == 0: 
        break
    T += 1
    N, D = M[0], M[1:]
    print("Case %d: %.1f" %( T, D[(N + 1)//2-1] if N%2 else (D[N//2-1] + D[(N//2)])/2))