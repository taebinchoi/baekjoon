for i in range(int(input())):
    tot = 0
    for j in input():
        if j == 'D':
            break
        tot += 1
    print(tot)