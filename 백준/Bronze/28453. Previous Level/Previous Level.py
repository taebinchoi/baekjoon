N = int(input())
M = list(map(int,input().split()))
K = []

for i in range(N):
    if M[i] == 300:
        K.append('1')
    elif 275 <= M[i] < 300:
        K.append('2')
    elif 250 <= M[i] < 275:
        K.append('3')
    else:
        K.append('4')
PL = ' '.join(str(i) for i in K)
print(PL)