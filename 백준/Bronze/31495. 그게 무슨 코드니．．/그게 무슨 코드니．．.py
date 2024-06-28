N = input()

if N[0] == N[-1] == '"' and len(N[1:-1])>0:
    print(N[1:-1])
else:
    print("CE")
