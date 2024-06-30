A, D, K = map(int,input().split())

if (K-A)%D == 0 and (K-A)//D >= 0:
    print(((K-A)//D)+1)
else:
    print('X')