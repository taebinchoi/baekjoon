N = int(input())

plus = 0
triple = 0

for i in range(1, N+1):
    plus += i
    triple += i**3
print(plus)
print(plus**2)
print(triple)