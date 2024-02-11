def F(N):
    if N <= 1:
        return N
    return F(N-1)+F(N-2)
M = int(input())
print(F(M))