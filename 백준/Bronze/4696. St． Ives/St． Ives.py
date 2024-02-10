while True:
    N = float(input())
    if N == 0:
        break
    print('%.2f'%(1 + N + N**2 + N**3 + N**4))