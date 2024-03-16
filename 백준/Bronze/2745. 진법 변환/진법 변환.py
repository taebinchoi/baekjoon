N, B = input().split()
N = N[::-1]
B = int(B)
num = 0
ls = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for i in range(len(N)):
    M = ls.index(N[i])
    num += M*pow(B, i)
print(num)