N = int(input())
for i in range(N):
    A, B, C = map(int,input().split())
    print(A, B, C)
    if A < 10 and B < 10 and C < 10:
        print('zilch')
    elif (A >= 10 and B < 10 and C < 10) or (B >= 10 and A < 10 and C < 10) or (C >= 10 and A < 10 and B < 10):
        print('double')
    elif (A >= 10 and B >= 10 and C < 10) or (A >= 10 and C >= 10 and B < 10) or (B >= 10 and C >= 10 and A < 10):
        print('double-double')
    else:
        print('triple-double')
    print(' ')