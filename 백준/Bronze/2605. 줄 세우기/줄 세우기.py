N = int(input())
M = list(map(int,input().split()))
K = []

for i in range(N):
    if M[i] == 0:
        K.insert(0, i+1)
    else:
        K.insert(M[i], i+1)

for i in reversed(K):
    print(i, end=' ')