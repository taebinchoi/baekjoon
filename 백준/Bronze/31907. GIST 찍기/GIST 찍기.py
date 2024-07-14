import sys
input = sys.stdin.readline

gist = ['G...', '.I.T', '..S.']
N = int(input())
for i in gist:
    L = ''
    for j in range(len(i)):
        L += (i[j]*N)
    for k in range(N):
        print(L)