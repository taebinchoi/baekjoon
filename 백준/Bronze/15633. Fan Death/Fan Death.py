N = int(input())
print(sum(i for i in range(1, N+1) if N%i == 0)*5-24)