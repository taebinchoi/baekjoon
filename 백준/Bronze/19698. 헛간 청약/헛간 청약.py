N, W, H, L = map(int,input().split())
A = (W//L)*(H//L)
print(min(A,N))