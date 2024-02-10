K, W, M = map(int,input().split())
if (W-K)%M == 0:
    print((W-K)//M)
else:
    print((W-K)//M+1)