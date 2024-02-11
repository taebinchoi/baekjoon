N = int(input())

for i in range(N):
    A, B, C = map(int, input().split())
    D = A
    E = B
    F = C
    for j in range(C):
        if A > B:
            A = A // 2
        else:
            B = B // 2
            
    if A >= B:
        print("Data set:", D, E, F)
        print(A, B)
    else:
        print("Data set:", D, E, F)
        print(B, A)
    print()
