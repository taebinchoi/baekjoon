result = 1
N = int(input())
M = int(input())
K = list(map(int,input().split()))
for i in range(len(K)):
    if M < K[i]:
        result += 1
        
print(result)