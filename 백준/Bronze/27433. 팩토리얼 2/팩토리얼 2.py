N = int(input())

if N == 0:
    print(1)
else:
    number = 1
    for i in range(2, N+1):
        number *= i
    print(number)