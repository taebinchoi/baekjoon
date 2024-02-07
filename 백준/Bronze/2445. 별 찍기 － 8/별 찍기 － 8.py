N = int(input())
1 <= N <= 100

for i in range(1, N):
    print("*"*i +" "*2*(N-i)+"*"*i)
for i in range(N, 0, -1):
    print("*"*i +" "*2*(N-i)+"*"*i)