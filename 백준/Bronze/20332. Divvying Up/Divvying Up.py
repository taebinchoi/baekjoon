N = input()
M = list(map(int, input().split()))

print(['no', 'yes'][sum(M)%3 == 0])