A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())
F = int(input())
100 >= A, B, C, D, E, F >= 0

print(A+B+C+D-min(A, B, C, D)+max(E, F))