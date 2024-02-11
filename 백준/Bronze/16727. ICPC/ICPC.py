P1, S1 = map(int,input().split())
S2, P2 = map(int,input().split())

if P1+P2 > S1+S2:
    print('Persepolis')
elif S1+S2 > P1+P2:
    print('Esteghlal')
else:
    if S1>P2:
        print('Esteghlal')
    elif S1<P2:
        print('Persepolis')
    else:
        print('Penalty')