N = int(input())
minute = list(map(int, input().split()))
Y = M = 0

for i in minute:
    Y += (i//30 + 1) * 10
    M += (i//60 + 1) * 15
if M == Y:
    print("Y M", M)
elif M < Y:
    print("M", M)
else:
    print("Y", Y)