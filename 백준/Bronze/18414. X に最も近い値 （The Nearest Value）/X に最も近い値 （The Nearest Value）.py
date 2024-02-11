X, L, R = map(int,input().split())
if (X >= R >= L):
    print(R)
elif (R >= X >= L):
    print(X)
else:
    print(L)