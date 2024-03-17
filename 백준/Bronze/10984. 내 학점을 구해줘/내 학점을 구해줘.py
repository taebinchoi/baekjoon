import sys
input = sys.stdin.readline
T = int(input())
for i in range(T):
    numA, numB = 0, 0
    N = int(input())
    for j in range(N):
        M, K = map(float,input().split())
        numA += M
        numB += M*K
    print("%d %.1f" %(numA, numB/numA))