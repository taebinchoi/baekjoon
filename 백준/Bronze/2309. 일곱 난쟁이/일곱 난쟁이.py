import itertools
seven = [int(input()) for i in range(9)]

for i in itertools.combinations(seven, 7):
    if sum(i) == 100:
        for j in sorted(i):
            print(j)
        break