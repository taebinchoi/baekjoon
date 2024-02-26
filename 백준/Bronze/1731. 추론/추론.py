N = int(input())
nums = []
for i in range(N):
    M = int(input())
    nums.append(M)
if nums[1]-nums[0] == nums[2]-nums[1]:
    print(nums[-1]+nums[1]-nums[0])
elif nums[1]/nums[0] == nums[2]/nums[1]:
    K = int(nums[1]/nums[0])
    print(nums[-1]*K)