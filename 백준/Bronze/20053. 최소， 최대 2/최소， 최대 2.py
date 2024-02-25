N = int(input())
for i in range(N):
    M = int(input())
    res = sorted(map(int, input().split()))
    print(res[0], res[-1])