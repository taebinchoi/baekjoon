N = int(input())

for q in range(N):
    M = int(input())
    K = int(input())
    
    per = [i for i in range(1, K+1)]
    for r in range(M):
        for j in range(1, K):
            per[j] += per[j-1]
    print(per[-1])