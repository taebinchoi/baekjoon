V = int(input())
T = list(str(input()))

A = B = 0
for V in T:
    if V == 'A':
        A += 1
    else:
        B += 1
if A > B:
    print('A')
elif A == B:
    print('Tie')
else:
    print('B')