N = int(input())
meal = list(map(int, input().split()))
final = 0

for i in range(3):
    if meal[i] <= N:
        final += meal[i]
    else:
        final += N

print(final)