T = int(input())
for i in range(1, T+1):
    A, B, C = map(int,input().split())
    if A + B <= C or A + C <= B or B + C <= A:
        print(f'Case #{str(i)}: invalid!')
    else:
        if A == B == C:
            print(f'Case #{str(i)}: equilateral')
        elif A == B != C or A == C != B or B == C != A:
            print(f'Case #{str(i)}: isosceles')
        else:
            print(f'Case #{str(i)}: scalene')