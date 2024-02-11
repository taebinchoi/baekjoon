N = int(input())
for _ in range(N):
    dog, dogfood, pound= map(float, input().split())
    total = dog*dogfood*pound
    print('$%.2f' % total)
