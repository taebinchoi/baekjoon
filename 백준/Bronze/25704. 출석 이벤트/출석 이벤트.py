N = int(input())
P = int(input())
N >= 0

Price = 0

if N >= 5:
    Price = max(Price, 500)
if N >= 10:
    Price = max(Price, P//10)
if N >= 15:
    Price = max(Price, 2000)
if N >= 20:
    Price = max(Price, P//4)

print(0 if P <= Price else P-Price)