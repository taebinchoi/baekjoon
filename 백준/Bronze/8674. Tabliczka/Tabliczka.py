A, B = map(int,input().split())
if A%2 == 0 or B%2 == 0:
    print(0)
else:
    print(min(A, B))