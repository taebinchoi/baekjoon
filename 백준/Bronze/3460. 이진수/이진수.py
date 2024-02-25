T = int(input())
for _ in range(T):
    N = int(input())
    M = bin(N)[2:]
    for i in range(len(M)):
        if M[::-1][i] == '1':
            print(i, end=' ')