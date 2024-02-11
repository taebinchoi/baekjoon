R, C, N = map(int, input().split())
row = 0
col = 0

if R % N:
    row = R // N+1
else:
    row = R // N
if C % N:
    col = C // N+1
else:
    col = C // N

print(row*col)