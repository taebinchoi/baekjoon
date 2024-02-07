M = int(input())
N = int(input())
tot = 0
min = 0

for i in range(1, 101):
    if M <= i**2 and N >= i**2:
        if tot == 0:
            min = i**2
        tot += i**2 #브루트포스의 활용

if tot == 0:
    print(-1)
else:
    print(tot)
    print(min)