N, W, H = map(int,input().split())
K = (W**2 + H**2)**0.5
for i in range(N):
    M = int(input())
    print("DA" if M <= K else "NE")