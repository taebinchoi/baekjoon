CH = SA = 100

for i in range(int(input())):
    A, B = map(int, input().split())
    if A > B:
        SA -= A
    elif A < B:
        CH -= B
        
print(CH)
print(SA)