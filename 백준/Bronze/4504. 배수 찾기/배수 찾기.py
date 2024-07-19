N = int(input())
M = int(input())
while M:
    if M%N == 0:
        print("%s is a multiple of %s."%(M, N))
    else:
        print("%s is NOT a multiple of %s."%(M, N))
    M = int(input())