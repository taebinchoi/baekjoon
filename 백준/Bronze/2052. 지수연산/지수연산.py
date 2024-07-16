N = int(input())
M = "%.300f"%2 ** -N
res = len(M)
for i in range(res-1, 1, -1):
    if M[i] != '0':
        res = i
        break
print(M[:res+1])