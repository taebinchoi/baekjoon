N = int(input())

for m in range(N):
    a = input()
    sco = 0
    sumSco = 0
    for n in a:
        if n == 'O':
            sco += 1
        else:
            sco = 0
        sumSco += sco
    print(sumSco)