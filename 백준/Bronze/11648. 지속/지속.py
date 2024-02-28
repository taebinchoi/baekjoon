N = input()
tot, happy = 0, 1
while True:
    if len(str(N)) == 1:
        print(tot)
        break
    for i in N:
        happy *= int(i)
    tot += 1    
    N = str(happy)
    happy = 1