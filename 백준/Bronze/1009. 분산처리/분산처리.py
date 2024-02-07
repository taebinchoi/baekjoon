T = int(input())
for i in range(T):
    A, B = map(int, input().split())
    A = A%10
    
    if A == 0:
        print(10)
    elif A == 1 or A == 5 or A == 6:
        print(A)
    elif A == 4 or A == 9:
        B = B%2
        if B == 1:
            print(A)
        else:
            print((A*A)%10)
    else:
        B = B%4
        if B == 0:
            print((A**4) % 10 % 10 % 10)
        else:
            print((A**B) % 10 % 10 % 10)