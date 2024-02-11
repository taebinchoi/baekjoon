import sys
N = int(input())
tot_list = [0] * 10001

for i in range(N):
    i_num = int(sys.stdin.readline())
    tot_list[i_num] = tot_list[i_num] + 1
    
for i in range(10001):
    if tot_list[i] != 0:
        for j in range(tot_list[i]):
            print(i)