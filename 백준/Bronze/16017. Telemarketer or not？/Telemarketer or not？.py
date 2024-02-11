A = int(input())
B = int(input())
C = int(input())
D = int(input())
if B == C:
    if A == 8 and D == 8:
        print('ignore')
    elif A == 8 and D == 9:
        print('ignore')
    elif A == 9 and D == 9:
        print('ignore')
    elif A == 9 and D == 8:
        print('ignore')
    else:
        print('answer')
else:
    print('answer')