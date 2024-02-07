N = int(input())
tot = 1

for i in range(N):
    tot += i*6
    if N <= tot:
        print(i+1)
        break