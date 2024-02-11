import math

W, H = map(int,input().split())
print(W+H-math.sqrt(W**2+H**2))