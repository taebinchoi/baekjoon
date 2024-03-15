P, Q = map(int, input().split())
A, B = 0, 0
for i in range(1, P+1):
    if P%i == 0:
        A += 1
    if A == Q:
        B = i
        break
print(B)