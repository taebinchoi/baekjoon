T = int(input())
1 <= T <= 10000
A = T//300
B = (T-300*A)//60
C = (T-300*A-60*B)//10

if T % 10 != 0:
    print(-1)
else:
    print(A, B, C)