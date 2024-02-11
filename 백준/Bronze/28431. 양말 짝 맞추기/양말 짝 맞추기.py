list1 = [int(input()) for J in range(5)]
set1 = set(list1)


for i in set1:
    if list1.count(i)%2 == 1:
        print(i)