A, B, C = map(int,input().split())

R = max([A, B, C])*3 - sum([A, B, C])
print(R)