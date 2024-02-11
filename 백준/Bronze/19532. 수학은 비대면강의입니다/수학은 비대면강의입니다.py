a, b, c, d, e, f = map(int,input().split())
for i in range(-999,1000):
    for j in range(-999,1000): #브루트포스, 이중for문
        if a*i+b*j == c and d*i+e*j == f:
            print(i, j)