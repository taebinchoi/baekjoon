N = list(map(int,input()))
N.sort(reverse=True)
result = 0

for i in N:
    result = result*10 + i
print(result)