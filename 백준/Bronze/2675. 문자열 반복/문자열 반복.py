N = int(input())

for i in range(N):
    a, b = input().split()
    for j in b:
        print(j*int(a), end = "")
    print()