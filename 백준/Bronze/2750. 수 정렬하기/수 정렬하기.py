N = int(input())
number_list = []

for i in range(N):
    number_list.append(int(input()))

new_list = sorted(number_list)

for i in range(len(number_list)):
    print(new_list[i])