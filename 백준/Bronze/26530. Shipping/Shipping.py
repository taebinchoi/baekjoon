N = int(input())
result = 0

for i in range(N):
    tot = 0
    M = int(input())
    for j in range(M):
        j, b, c = input().split()
        tot += float(b)*float(c)
        
    print(f'${tot:0.2f}')