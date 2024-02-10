s = 0

while True:
    N = int(input())
    s += 1
    
    if N == 0:
        break
    if N % 2!=0:
        print(s, ". odd ", N//2, sep='')
    else:
        print(s, ". even ", N//2, sep='')