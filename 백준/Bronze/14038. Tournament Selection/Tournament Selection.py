winlose = [input() for i in range(6)]
win = winlose.count('W')

if win >= 5:
    print(1)
elif win >= 3:
    print(2)
elif win >= 1:
    print(3)
else:
    print(-1)