P, R = map(int,input().split())
V = P/R
if V < 0.2:
    print('weak')
elif 0.2 <= V < 0.4:
    print('normal')
elif 0.4 <= V < 0.6:
    print('strong')
else:
    print('very strong')