T = int(input())

for j in range(T):
    N = int(input())
    total = 0
    for i in range(N):
        if i%2 == 1:
            total += i
    print(total + N)