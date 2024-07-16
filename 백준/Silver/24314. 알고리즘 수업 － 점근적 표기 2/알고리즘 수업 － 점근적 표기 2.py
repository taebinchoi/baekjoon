A1, A0 = map(int,input().split())
C = int(input())
N = int(input())

for i in range(N, 102):
    if A1*i+A0 < C*i:
        print(0)
        break
else:
    print(1)