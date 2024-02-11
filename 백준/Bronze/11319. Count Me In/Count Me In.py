S = int(input())
for i in range(S):
    N = input()
    N = N.replace(" ","") #띄어쓰기 없애기
    M = len(N)
    A = N.count('A')
    B = N.count('E')
    C = N.count('I')
    D = N.count('O')
    E = N.count('U')
    F = N.count('a')
    G = N.count('e')
    H = N.count('i')
    I = N.count('o')
    J = N.count('u')
    K = A+B+C+D+E+F+G+H+I+J
    print((M-K),K)