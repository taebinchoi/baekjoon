N = int(input())
S = input()
L = len(S)
check = 0

for i in range(0, L-2):
    if (S[i] == 'o') and (S[i+1] == 'o') and (S[i+2] == 'o'):
        check += 1

if check != 0:
    print('Yes')
else:
    print('No')