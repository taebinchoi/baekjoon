N = int(input())
M = list(map(int,input().split()))
tot, plus = 0, 0

for i in range(N):
    if M[i]==1:
        plus = plus+1
    else:
        plus = 0
    tot = tot + plus
print(tot)