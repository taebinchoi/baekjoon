T = int(input())
for i in range(T):
    N = int(input())
    for _ in range(N):
        A = list(map(int,input().split()))
        print((A[0]+A[1]), (A[0]*A[1]))