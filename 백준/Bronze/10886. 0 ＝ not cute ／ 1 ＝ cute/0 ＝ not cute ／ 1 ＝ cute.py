N = int(input())
N%2 == 1

M = 0

for i in range(N):
    if int(input()) == 1:
        M += 1

if M > N//2:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")