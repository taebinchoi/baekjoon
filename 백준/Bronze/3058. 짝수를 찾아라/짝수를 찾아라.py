N = int(input())
for i in range(N):
    even = 0
    K = []
    M = list(map(int,input().split()))
    for j in M:
        if j % 2 == 0:
            even += j
            K.append(j)
    print(even, int(min(K)))