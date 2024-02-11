def exist(D, A, K):
    for i in range(1, D):
        for j in range(1, D):
            if i * A + j * K == D:
                return 1
    return 0

D, A, K = map(int, input().split())

result = exist(D, A, K)
print(result)