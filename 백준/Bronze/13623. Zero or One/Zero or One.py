A, B, C = map(int,input().split())
if A == B == C:
    print('*')
if A == B != C:
    print('C')
if A == C != B:
    print('B')
if B == C != A:
    print('A')