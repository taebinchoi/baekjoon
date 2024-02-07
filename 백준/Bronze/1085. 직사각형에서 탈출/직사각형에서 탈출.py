X, Y, W, H = map(int,input().split())
print(min([X, Y, H-Y, W-X]))