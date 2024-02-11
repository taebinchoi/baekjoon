for i in range(int(input())):
    M, A, B = map(str,input().split())
    A, B = int(A), int(B)
    M = M[:A] + M[B:]
    print(M)