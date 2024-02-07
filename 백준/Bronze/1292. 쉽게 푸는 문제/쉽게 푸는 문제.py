A, B = map(int,input().split())
problem = [0]
sum = 0

for i in range(1, B+1):
    for j in range(i):
        problem.append(i)

for i in range(A, B+1):
    sum += problem[i]
print(sum)