import sys
input = sys.stdin.readline
x = []
y = []

N = int(input())
for i in range(N):
    M, K = map(int,input().split())
    x.append(M)
    y.append(K)
print((max(x)-min(x))*(max(y)-min(y)))