N = int(input())
print('Gnomes:')
for i in range(N):
    A, B, C = map(int,input().split())
    if A < B < C or A > B > C:
        print('Ordered')
    else:
        print('Unordered')