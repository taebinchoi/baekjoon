import sys
input = sys.stdin.readline
 
N = int(input())
stick = [int(input()) for i in range(N)]
high = stick[-1]
tot = 1
 
for j in range(N):
    if high < stick[N-j-1]:
        tot += 1
        high = stick[N-j-1]
        
print(tot)