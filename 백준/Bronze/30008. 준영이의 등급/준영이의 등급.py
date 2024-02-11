N, K = map(int, input().split())
G = list(map(int, input().split()))
tot = []

for i in G:
    P = (i*100)//N
    if 0 <= P <= 4:
        tot.append(1)
    elif 4 < P <= 11:
        tot.append(2)
    elif 11 < P <= 23:
        tot.append(3)
    elif 23 < P <= 40:
        tot.append(4)
    elif 40 < P <= 60:
        tot.append(5)
    elif 60 < P <= 77:
        tot.append(6)
    elif 77 < P <= 89:
        tot.append(7)
    elif 89 < P <= 96:
        tot.append(8)
    elif 96 < P <= 100:
        tot.append(9)

print(*tot, sep=' ')