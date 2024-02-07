N = int(input())
M = list(map(int,input().split()))
tot = 0

for i in M:
    K = 0
    if i == 1:
        continue
    for j in range(2, i):
        if i % j == 0:
            K = 1
    if K == 0:
        tot += 1   

print(tot)