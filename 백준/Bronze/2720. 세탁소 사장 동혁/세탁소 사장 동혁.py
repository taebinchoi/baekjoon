N = int(input())
for i in range(N):
    A = int(input())
    B = A//25
    C = (A-B*25)//10
    D = (A-B*25-C*10)//5
    E = A-B*25-C*10-D*5
    print(B, C, D, E)