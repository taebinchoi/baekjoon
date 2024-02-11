T = int(input())
while T > 0 :
    A, B, C = map(int,input().split())
    print(min(A, min(B, C)))
    T -= 1