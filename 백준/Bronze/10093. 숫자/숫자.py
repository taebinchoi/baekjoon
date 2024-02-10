A, B = map(int,input().split())
A >= 1 and A <= 1000
B >= 1 and B <= 1000

if A > B:
  print(A-B-1)
  for i in range(B+1, A):
    print(i)
elif B > A:
  print(B-A-1)
  for i in range(A+1, B):
    print(i)
else:
  print(0)