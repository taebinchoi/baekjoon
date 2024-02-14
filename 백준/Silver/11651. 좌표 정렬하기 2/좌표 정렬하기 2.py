N = int(input())
lis = []

for i in range(N):
    [M, K] = map(int, input().split())
    lis.append([M, K])
    
lis.sort(key = lambda x : (x[1],x[0]))
for i in lis:
    print(i[0], i[1])