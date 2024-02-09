a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

list = [a, b, c, d, e]
list.sort()

print(int(sum(list)/len(list)))
print(list[2])