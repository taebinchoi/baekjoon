L, R = map(int,input().split())
if L == 0 and R == 0:
    print('Not a moose')
elif L == R:
    print('Even', str(L+R))
else:
    print('Odd', str(2*max(L, R)))
    