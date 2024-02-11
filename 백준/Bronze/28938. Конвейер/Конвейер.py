N = int(input())
numbers = list(map(int, input().split()))

if sum(numbers) > 0:
    print('Right')
elif sum(numbers) == 0:
    print('Stay')
else:
    print('Left')
