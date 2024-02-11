N = int(input())
hot = 0

for i in range(N):
    M = input()
    if M == 'Poblano':
        hot += 1500
    if M == 'Mirasol':
        hot += 6000
    if M == 'Serrano':
        hot += 15500
    if M == 'Cayenne':
        hot += 40000
    if M == 'Thai':
        hot += 75000
    if M == 'Habanero':
        hot += 125000
print(hot)