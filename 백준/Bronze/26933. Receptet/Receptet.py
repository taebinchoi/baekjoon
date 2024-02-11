N = int(input())
amount = 0

for i in range(N):
    H, B, K = map(int,input().split())
    if H >= B:
        continue
    else:
        amount += (B-H)*K
print(amount)