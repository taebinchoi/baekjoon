while 1:
    N = int(input())
    if N == 0:
        break
    sum = 0
    for i in range(1, N+1):
        sum = sum + i
    print(sum)