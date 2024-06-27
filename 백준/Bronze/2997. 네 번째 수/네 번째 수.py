import sys
input = sys.stdin.readline

N = list(map(int,input().split()))
N.sort()

if N[1]-N[0] == N[2]-N[1]:
    print(N[2]*2-N[1])
elif N[1]-N[0] > N[2]-N[1]:
    print(N[1]*2-N[2])
else:
    print(N[1]*2-N[0])