X1, Y1, X2, Y2 = map(int,input().split())
X3, Y3, X4, Y4 = map(int,input().split())

M = max(X2, X4)-min(X1, X3)
N = max(Y2, Y4)-min(Y1, Y3)
print(max(M, N)**2)