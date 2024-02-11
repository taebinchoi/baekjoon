N = int(input())
score = []
for i in range(N):
    A, D, G = map(int,input().split())
    if A == D+G:
        sc1 = 2*A*(D+G)
        score.append(sc1)
    else:
        sc2 = A*(D+G)
        score.append(sc2)
print(max(score))