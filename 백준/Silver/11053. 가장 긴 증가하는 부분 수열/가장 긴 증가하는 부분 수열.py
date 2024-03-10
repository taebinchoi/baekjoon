N = int(input())
M = list(map(int, input().split()))
K = [1 for i in range(N)]

for j in range(N):
    for k in range(j):
        if M[j]>M[k]:
            K[j] = max(K[k]+1, K[j])
        
print(max(K))