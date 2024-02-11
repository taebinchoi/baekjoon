T = int(input())
M = list(map(int, input().split()))
if T < 5:
    M += [0]*(5-T)
tot = 0

if M[0] > M[2]:
    tot += (M[0]-M[2])*508
else:
    tot += abs(M[0]-M[2])*108
if M[1] > M[3]:
    tot += (M[1]-M[3])*212
else:
    tot += abs(M[1]-M[3])*305
if M[4] != 0:
    tot += M[4]*707

print(tot*4763)