while True:
    N = int(input())
    if N%42 == 0 and N != 0:
        print('PREMIADO')
    if N%42 != 0:
        print('TENTE NOVAMENTE')
    if N == 0:
        break