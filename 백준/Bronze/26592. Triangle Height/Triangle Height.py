N = int(input())
for i in range(N):
    A, B = map(float,input().split())
    C = 2*A/B
    print('The height of the triangle is {:.2f} units'.format(C))