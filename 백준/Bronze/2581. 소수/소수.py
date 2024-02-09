M = int(input())
N = int(input())

tot = []
for i in range(M, N+1):
    situation = 0
    if i > 1:
        for j in range(2,i):
            if i % j == 0:
                situation += 1
                break
        if situation == 0:
            tot.append(i)

if len(tot) < 1:
    print(-1)
else:
    print(sum(tot))
    print(min(tot))