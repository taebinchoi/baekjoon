A = []
for i in range(10):
    N = int(input())
    N = A.append(N%42)

A = set(A)
print(len(A))