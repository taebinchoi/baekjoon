numbers = [i for i in range(1, 31)]

for o in range(28):
    num = int(input())
    numbers.remove(num)

print(min(numbers))
print(max(numbers))