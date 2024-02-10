import sys
input = sys.stdin.readline

N = int(input())
ascore, bscore = 0, 0
for i in range(N):
    A, B = map(int,input().split())
    if A > B:
        ascore += 1
    if B > A:
        bscore += 1
        
print(ascore, bscore)