import sys

T = int(input())
for i in range(1, T + 1):
    i = i + 1
    x, y = sys.stdin.readline().split()
    print(int(x) + int(y))