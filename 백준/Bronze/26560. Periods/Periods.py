N = int(input())
for i in range(N):
    M = str(input())
    if M[-1] == '.':
        print(M)
    else:
        print(M+'.')
        