N = int(input())
for i in range(N):
    M = input()
    if M == "P=NP":
        print("skipped")
    else:
        A, B = map(int, M.split('+'))
        print(A+B)