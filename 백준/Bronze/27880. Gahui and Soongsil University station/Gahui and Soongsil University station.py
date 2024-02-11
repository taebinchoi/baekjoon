totstair = 0
for i in range(4):
    M, N = input().split()
    N = int(N)
    if M == 'Es':
        totstair += N*21
    if M == 'Stair':
        totstair += N*17
        
print(totstair)