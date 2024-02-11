N = int(input())
money = 0
for i in range(N):
    M, K = map(int,input().split())
    if M == 136:
        money += 1000
    if M == 142:
        money += 5000
    if M == 148:
        money += 10000
    if M == 154:
        money += 50000
print(money)