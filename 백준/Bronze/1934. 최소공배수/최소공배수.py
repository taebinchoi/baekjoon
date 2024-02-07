N = int(input())
 
for i in range(N):
    M, K = map(int,input().split())
    N1 = M
    N2 = K
    while N2 != 0:
        temp = N1
        N1 = N2
        N2 = temp % N2
   
    print(M*K//N1)