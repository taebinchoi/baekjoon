N = int(input())
S = input()
V = 0

for i in S:
    if i in ['a', 'e', 'i', 'o', 'u']:
        V += 1
print(V)