N = int(input())
for i in range(N):
    A, B = map(float,input().split())
    print(round(abs(A-B),1))