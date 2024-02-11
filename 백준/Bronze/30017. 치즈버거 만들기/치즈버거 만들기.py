A, B = map(int,input().split())
sta = 3

A -= 2
B -= 1
K = min(A, B)

sta += (2*K)
print(sta)