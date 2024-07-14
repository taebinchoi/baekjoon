A1, A2 = map(int,input().split())
B1, B2 = map(int,input().split())

M = A2//B1 + (1 if A2%B1 else 0)
N = B2//A1 + (1 if B2%A1 else 0)

if M == N:
    print("DRAW")
elif M > N:
    print("PLAYER A")
else:
    print("PLAYER B")