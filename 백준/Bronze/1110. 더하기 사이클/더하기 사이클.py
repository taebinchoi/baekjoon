N = int(input())
number = N
tr = 0

while True:
    p = number // 10
    q = number % 10
    r = (p+q) % 10
    number = (q*10) + r

    tr = tr + 1
    if (number == N):
        break

print(tr)