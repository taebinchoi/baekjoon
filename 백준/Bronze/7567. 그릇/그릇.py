N = list(str(input()))
tot = 0
for i in range(len(N)):
    if i == 0:
        tot += 10
    elif N[i] == N[i-1]:
        tot += 5
    else:
        tot += 10

print(tot)