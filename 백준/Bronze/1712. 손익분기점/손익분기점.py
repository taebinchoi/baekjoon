A, B, C = map(int,input().split())
if C != B:
    D = int(A/(C-B))+1
    if C > B:
        print(D)
    else:
        print(-1)
else:
    print(-1)