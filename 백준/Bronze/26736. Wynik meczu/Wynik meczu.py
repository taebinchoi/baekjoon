M = list(input())
A, B = 0, 0
for i in range(len(M)):
    if M[i] == 'A':
        A += 1
    if M[i] == 'B':
        B += 1
print(f'{A} : {B}')