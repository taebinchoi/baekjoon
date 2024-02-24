import sys 
input = sys.stdin.readline
M = int(input())
for _ in range(M):
    option = 0
    S = int(input())
    N = int(input())
    for _ in range(N):
        Q, P = map(int,input().split())
        option += Q*P
    print(S+option)