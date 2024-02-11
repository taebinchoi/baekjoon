N = int(input())

for i in range (N):
    A, B, C, D = map(int, input().split())
    if A*B > C*D:
        print("TelecomParisTech")
    elif A*B < C*D:
        print("Eurecom")
    else :
        print("Tie")