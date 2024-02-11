N = int(input())
for i in range(N):
    A, B = input().split()
    C = int(B)
    if 97 <= C <= 100:
        print(A, 'A+')
    elif 90 <= C <= 96:
        print(A, 'A')
    elif 87 <= C <= 89:
        print(A, 'B+')
    elif 80 <= C <= 86:
        print(A, 'B')
    elif 77 <= C <= 79:
        print(A, 'C+')
    elif 70 <= C <= 76:
        print(A, 'C')
    elif 67 <= C <= 69:
        print(A, 'D+')
    elif 60 <= C <= 66:
        print(A, 'D')
    else:
        print(A, 'F')