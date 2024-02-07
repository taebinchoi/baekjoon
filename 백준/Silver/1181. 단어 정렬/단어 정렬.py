N = int(input())
W = [str(input()) for i in range(N)]
W = list(set(W))

W.sort()
W.sort(key=len)

for i in W:
    print(i)