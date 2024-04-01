N = int(input())
for i in range(N):
    M = list(map(int, input().split()))
    K = [M[j] + M[j+4] for j in range(4)]
    tot = max(K[0], 1) + max(K[1], 1)*5 + max(K[2], 0)*2 + K[3]*2
    print(tot)