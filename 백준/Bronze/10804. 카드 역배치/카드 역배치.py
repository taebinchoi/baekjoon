import sys
input = sys.stdin.readline

card = [i for i in range(1, 21)]
for i in range(10):
    M, N = map(int,input().split())
    M -= 1
    card[M:N] = card[M:N][::-1] #슬라이싱
    
print(*card)