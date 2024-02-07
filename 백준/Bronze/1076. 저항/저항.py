resis = {'black' : 0, 'brown': 1, 'red': 2, 'orange': 3, 'yellow': 4, 'green': 5, 'blue': 6, 'violet': 7, 'grey': 8, 'white': 9}
A = input()
B = input()
C = input()

final = str(resis[A]) + str(resis[B]) 
final = int(final) * (10**resis[C])

print(final)