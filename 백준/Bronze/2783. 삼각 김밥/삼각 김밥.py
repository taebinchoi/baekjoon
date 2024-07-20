X, Y = map(int,input().split())
res = [X/Y]
for i in range(int(input())):
    X, Y = map(int,input().split())
    res.append(X/Y)
print("%.2f" % (min(res)*1000))