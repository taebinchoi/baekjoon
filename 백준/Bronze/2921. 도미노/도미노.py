N = int(input())
dot = 0

for i in range(N+1):
    for j in range(i, N+1):
        dot += (i+j)
print(dot)