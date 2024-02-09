while True:
    A, B, C = map(int,input().split())
    if A == B == C == 0:
        break
    elif A**2 + B**2 == C**2 or A**2 + C**2 == B**2 or B**2 + C**2 == A**2:
        print('right')
    else:
        print('wrong')