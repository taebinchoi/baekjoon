l = []
for _ in range(int(input())):
    a, b, c = map(int, input().split())
    if a == b and b == c:
        l.append(10000 + a*1000)
    elif a == b:
        l.append(1000 + a*100)
    elif b == c:
        l.append(1000 + b*100)
    elif c == a:
        l.append(1000 + c*100)
    else:
        l.append(max(a, b, c)*100)
        
print(max(l))