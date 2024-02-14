apple = 0

for i in range(int(input())):
    M, N = map(int, input().split())
    apple += N % M
print(apple)