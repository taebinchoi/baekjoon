A = sorted(map(int,input().split()))
r = A[0] + A[1] + min(A[2], A[0]+A[1]-1)

print(r)