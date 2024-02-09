A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))
D = list(map(int,input().split()))
E = list(map(int,input().split()))
F = int(max(sum(A), sum(B), sum(C), sum(D), sum(E)))

if F == sum(A):
    print(1, F)
if F == sum(B):
    print(2, F)
if F == sum(C):
    print(3, F)
if F == sum(D):
    print(4, F)
if F == sum(E):
    print(5, F)