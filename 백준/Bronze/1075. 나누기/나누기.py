N, F = input(), input()
K = int(N[:-2]+'00')

while True:
    if K%int(F) == 0:
        break
    K += 1
K = str(K)

print(K[-2:])