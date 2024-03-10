M = int(input())
if M <= 30:
    N = M/2
else:
    N = (M-30)*1.5+15
print(round(N,1))