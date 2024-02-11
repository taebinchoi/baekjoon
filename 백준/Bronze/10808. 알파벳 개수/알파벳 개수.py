N = input()
tot = [0]*26

for i in N:
    tot[ord(i)-97] += 1

print(*tot)