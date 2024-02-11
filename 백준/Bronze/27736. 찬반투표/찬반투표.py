N = int(input())
M = list(map(int,input().split()))

if M.count(0)>= N/2:
    print("INVALID")
else:
    if M.count(1) > M.count(-1):
        print("APPROVED")
    else:
        print("REJECTED")