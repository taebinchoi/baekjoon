number = int(input())
s = input()
two = 0
e = 0
for i in range(number):
    if s[i] == 'e':
        e = e + 1
    else:
        two = two + 1
if e > two:
    print('e')
elif e == two:
    print('yee')
else:
    print(2)