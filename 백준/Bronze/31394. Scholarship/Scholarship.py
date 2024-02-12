N = int(input())
K = []

for i in range(N):
    M = int(input())
    K.append(M)
L = sum(K)

if K.count(3) != 0:
    print('None')
else:
    if L/N == 5:
        print('Named')
    elif 4.5 <= L/N < 5:
        print('High')
    else:
        print('Common')