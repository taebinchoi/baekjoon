N = int(input())
lis = []

for i in range(N):
    [M, K] = map(int, input().split())
    lis.append([M, K])
    
lis.sort()
for i in lis:
    print(i[0], i[1])