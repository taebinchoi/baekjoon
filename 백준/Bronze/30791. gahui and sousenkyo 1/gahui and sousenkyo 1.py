A, B, C, D, E = map(int,input().split())
rate = 0
if A-B <= 1000:
    rate += 1
if A-C <= 1000:
    rate += 1
if A-D <= 1000:
    rate += 1
if A-E <= 1000:
    rate += 1
print(rate)