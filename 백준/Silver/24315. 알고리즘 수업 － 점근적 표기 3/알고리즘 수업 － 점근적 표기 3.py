A1, A0 = map(int,input().split())
C1, C2 = map(int,input().split())
N = int(input())

for i in range(N, 101):
    if not C1*i <= A1*i+A0 <= C2*i:
        print(0)
        break
else:
    print(1)