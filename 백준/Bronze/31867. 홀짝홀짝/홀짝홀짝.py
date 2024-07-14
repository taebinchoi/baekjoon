N = int(input())
K = input()
odd, eve = 0, 0

for i in K:
    if int(i)%2 != 0:
        odd += 1
    else:
        eve += 1

if odd>eve:
    print(1)
elif odd<eve:
    print(0)
else:
    print(-1)