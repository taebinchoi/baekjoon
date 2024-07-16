while True:
    N = list(map(int,input().split()))
    if N == [0]:
        break
    for i in range(N[0]//4):
        M = [2*i+1, 2*i+2, N[0]-2*i-1, N[0]-2*i]
        if N[1] in M:
            M.remove(N[1])
            print(*M)