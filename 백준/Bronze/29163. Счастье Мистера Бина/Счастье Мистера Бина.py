N = int(input())
numbers = list(map(int, input().split()))

even_count = 0
odd_count = 0

for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

if even_count > odd_count:
    print('Happy')
else:
    print('Sad')
