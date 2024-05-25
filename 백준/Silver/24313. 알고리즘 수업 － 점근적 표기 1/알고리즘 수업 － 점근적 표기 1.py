A1, A0 = map(int, input().split())
M = int(input())
N = int(input())

if (A1*N+A0)<=(M*N) and A1<=M:
    print(1)
else:
    print(0)