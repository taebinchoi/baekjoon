A, B, C, D, N = map(int, input().split())
E = (A+B+C+D) / 4
F = (A+B+C+D) // 4

if E >= N:
    print(0)
else:
    H = A+B+C+D
    if H%4 == 0:
        print("%g" %(4*(N-E)))
    else:
        print("%g" %(4*N-H))