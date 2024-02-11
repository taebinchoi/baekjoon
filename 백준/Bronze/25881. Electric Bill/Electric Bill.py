M, N = map(int,input().split())
J = int(input())
for i in range(J):
    K = int(input())
    if K > 1000:
        print(K, 1000*M+(K-1000)*N)
    elif K <= 1000:
        print(K, K*M)