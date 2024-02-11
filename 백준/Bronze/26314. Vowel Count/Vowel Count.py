N = int(input())

for i in range(N):
    M = str(input())
    K1 = M.count('a')
    K2 = M.count('e')
    K3 = M.count('i')
    K4 = M.count('o')
    K5 = M.count('u')
    L = len(M)-int(K1+K2+K3+K4+K5)
    if (K1+K2+K3+K4+K5) > L:
        print(M, '1', end='\n')
    else:
        print(M, '0', end='\n')