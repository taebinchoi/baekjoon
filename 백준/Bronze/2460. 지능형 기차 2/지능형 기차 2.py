num = 0
tot = []

for i in range(1,11):
    A, B = list(map(int,input().split()))
    num = num-A+B
    tot.append(num)

tot.sort()
print(tot[-1])