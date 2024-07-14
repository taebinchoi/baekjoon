N = int(input())
L = list(map(int,input().split()))
res = sorted(set(L))

for i in res:
    print(int(i))