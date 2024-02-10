N = int(input())

for i in range(N):
    C, V = map(int,input().split())
    A, B = C//V, C%V
    print('You get '+str(A)+' piece(s) and your dad gets '+str(B)+' piece(s).')