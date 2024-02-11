N = input()
m1 = int(N[5])
m2 = int(N[6])
d = int(N[8:10])

if m1 == 1:
    print('TOO LATE')
else:
    if m2 <= 8:
        print('GOOD')
    elif m2 == 9 and 1 <= d <= 16:
        print('GOOD')
    else:
        print('TOO LATE')