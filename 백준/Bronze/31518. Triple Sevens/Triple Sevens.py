N = int(input())
jackpot = 0
for i in range(3):
    M = list(input().split())
    if '7' in M:
        jackpot += 1
if jackpot == 3:
    print(777)
else:
    print(0)