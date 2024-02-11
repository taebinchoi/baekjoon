A, B = map(int,input().split())

C = A*(100-B)/100

if C >= 100:
    print(0)
else:
    print(1)