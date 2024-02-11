N = int(input())
M = input()
rainbowupper = 'ROYGBIV'
rainbowlower = 'roygbiv'

if all(color in M for color in rainbowupper) and all(color in M for color in rainbowlower):
    print('YeS')
elif all(color in M for color in rainbowupper):
    print('YES')
elif all(color in M for color in rainbowlower):
    print('yes')
else:
    print('NO!')
