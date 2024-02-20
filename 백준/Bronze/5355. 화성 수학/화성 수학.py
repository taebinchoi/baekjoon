N = int(input())
for i in range(N):
    M = list(input().split())
    tot = float(M.pop(0))
    for j in range(len(M)):
        if M[j] == '@':
            tot *= 3
        elif M[j] == '%':
            tot += 5
        elif M[j] == '#':
            tot -= 7
    
    print("%0.2f" % tot)