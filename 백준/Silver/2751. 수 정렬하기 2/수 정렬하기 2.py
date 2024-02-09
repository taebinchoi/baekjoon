N = int(input())
nums = []
for i in range(N):
    M = int(input())
    nums.append(M)
nums.sort()

for i in range(N):
    print(nums[i])