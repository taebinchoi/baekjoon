N = int(input())
change = 1000-N
moneys = [500, 100, 50, 10, 5, 1]
count = 0

for i in moneys:
    count += change//i
    change %= i

print(count)