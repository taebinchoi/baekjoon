N = int(input())
M = N%8

if M != 0 and M <= 5:
    print(M)
else:
    if M == 0:
        print('2')
    else:
        M = 10 - M
        print(M)