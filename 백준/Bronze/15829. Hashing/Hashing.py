N = int(input())
M = 1234567891
K = 31
L = input()
 
tot = 0
for i in range(len(L)):
    num = ord(L[i]) - 96
    tot += num * (K ** i)
 
print(tot % M)