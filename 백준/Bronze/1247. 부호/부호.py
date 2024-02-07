import sys
input = sys.stdin.readline

for i in range(3):
    N = int(input())
    tot = 0
    for j in range(N):
        tot += int(input())
    if tot == 0:
        print(0)
    elif tot > 0:
        print("+")
    else:
        print("-")