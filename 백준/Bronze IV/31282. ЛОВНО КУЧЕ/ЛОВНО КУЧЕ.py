A, B, C = map(int, input().split())
D = A//(C-B)
if A%(C-B) != 0:
    D += 1

print(D)
