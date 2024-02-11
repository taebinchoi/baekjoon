T = int(input())
N = int(input())
F = list(map(int,input().split()))
G = sum(F)
if G >= T:
    print('Padaeng_i Happy')
else:
    print('Padaeng_i Cry')
