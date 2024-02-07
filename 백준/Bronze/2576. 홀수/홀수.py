odd = []
for i in range(7):
    full = int(input())
    if full % 2 == 1:
        odd.append(full)
if len(odd) == 0:
    print('-1')
else:
    print(sum(odd))
    print(min(odd))