N = int(input())
M = input()
K = int(input())

if M == "annyong":
    if K%2 == 1:
        print(K)
    else:
        print(K-1)
if M == "induck":
    if K%2 == 0:
        print(K)
    else:
        if N == K:
            print(K-1)
        else:
            print(K+1)