N = int(input())
result = []
A, B = N%12, N%10

if A == 9:
    result.append('F')
if A == 10:
    result.append('G')
if A == 11:
    result.append('H')
if A == 0:
    result.append('I')
if A == 1:
    result.append('J')
if A == 2:
    result.append('K')
if A == 3:
    result.append('L')
if A == 4:
    result.append('A')
if A == 5:
    result.append('B')
if A == 6:
    result.append('C')
if A == 7:
    result.append('D')
if A == 8:
    result.append('E')
if B == 3:
    result.append('9')
if B == 4:
    result.append('0')
if B == 5:
    result.append('1')
if B == 6:
    result.append('2')
if B == 7:
    result.append('3')
if B == 8:
    result.append('4')
if B == 9:
    result.append('5')
if B == 0:
    result.append('6')
if B == 1:
    result.append('7')
if B == 2:
    result.append('8')

print(''.join(str(i) for i in result))