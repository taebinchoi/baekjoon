D, H, W = map(int,input().split())
K = (H*H + W*W)**(1/2)
L = D/K

M = int(H*L)
N = int(W*L)

print("%d %d" %(M, N))