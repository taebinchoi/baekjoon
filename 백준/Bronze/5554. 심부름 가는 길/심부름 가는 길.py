A = int(input())
B = int(input())
C = int(input())
D = int(input())

60 <= A+B+C+D <= 3599
x = (A+B+C+D)//60
y = (A+B+C+D)%60
print(x)
print(y)