N1, N2, N12 = map(int,input().split())
0 <= N1, N2 <= 10000
0 <= N12 <= min(N1, N2)

N = print((N1+1)*(N2+1)//(N12+1)-1)