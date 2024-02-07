import sys
import math

B_size = int(sys.stdin.readline())
B = sys.stdin.readline().replace("\n", "").split(' ')
B = [int(i) for i in B]

sorted_B = [i for i in B]
sorted_B.sort()

P = []

for i in B:
    P.append(sorted_B.index(i))
    sorted_B[sorted_B.index(i)] = -1

results = [i for i in P]

for result in results:
    sys.stdout.write(str(result)+' ')