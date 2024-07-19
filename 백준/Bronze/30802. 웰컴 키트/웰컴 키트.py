N = int(input())
size = list(map(int,input().split()))
T, P = map(int,input().split())
A = 0
for i in range(len(size)):
    if size[i]%T == 0:
        A += int(size[i]/T)
    else:
        A += (int(size[i]/T)+1)
print(A)
print(int(N/P), N%P)