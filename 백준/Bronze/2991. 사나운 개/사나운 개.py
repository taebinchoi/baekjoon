A, B, C, D = map(int,input().split())
K = list(map(int, input().split()))

for i in K:
    tot = 0
    if 0 < i%(A+B) <= A:
        tot += 1
    if 0 < i%(C+D) <= C:
        tot += 1
    print(tot)