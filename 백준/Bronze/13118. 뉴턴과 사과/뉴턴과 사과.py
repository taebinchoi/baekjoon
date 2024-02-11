P = list(map(int,input().split()))
x, y, r = map(int,input().split())

if x in P:
    print(P.index(x)+1)
else:
    print(0)