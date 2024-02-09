N, M = map(int, input().split())
C = list(map(int, input().split()))

tot = 0
maxnum = 0

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            tot = C[i] + C[j] + C[k]
            if tot <= M and tot > maxnum:
                maxnum = tot

print(maxnum)