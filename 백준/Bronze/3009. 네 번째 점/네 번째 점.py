x_nums = []
y_nums = []
for _ in range(3):
    x, y = map(int, input().split())
    x_nums.append(x)
    y_nums.append(y)

for j in range(3):
    if x_nums.count(x_nums[j]) == 1:
        z = x_nums[j]
    if y_nums.count(y_nums[j]) == 1:
        w = y_nums[j]
print(z, w)