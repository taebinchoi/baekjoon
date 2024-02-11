import sys
input = sys.stdin.readline

N = int(input())
nums = []
for i in range(N):
    M = int(input())
    nums.append(M)
nums.sort(reverse=True)

for i in range(N):
    print(nums[i])