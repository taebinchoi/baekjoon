import sys
input = sys.stdin.readline
N = int(input())

week = 1
for i in range(11, N+1):
    week *= i
    
print(6*week)