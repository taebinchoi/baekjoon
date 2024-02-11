N = int(input())
for i in range(N):
    C, P = map(int,input().split())
    print(C, P)
    if C == 1:
        print(P)
    else:
        print(P+(P-2)*(C-1))