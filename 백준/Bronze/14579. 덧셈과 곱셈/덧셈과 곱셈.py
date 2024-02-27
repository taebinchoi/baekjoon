A, B = map(int,input().split())
tot = int(A*(A+1)/2)
for i in range(A+1, B+1):
    tot *= int(i*(i+1)/2)

print(tot%14579)