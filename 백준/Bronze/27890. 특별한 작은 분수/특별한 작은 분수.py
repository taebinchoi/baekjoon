def special(X, N):
    for i in range(N):
        if X%2 == 0:
            X = int(X/2) ^ 6
        else:
            X = (2*X) ^ 6
    return X

if __name__ == '__main__':
    X, N = map(int, input().split())
    print(special(X, N))