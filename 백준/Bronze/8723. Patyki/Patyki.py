L = sorted(map(int, input().split()))
if L[0] == L[1] == L[2]:
    print(2)
elif L[0]**2 + L[1]**2 == L[2]**2:
    print(1)
else:
    print(0)