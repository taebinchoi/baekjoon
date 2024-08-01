def play(N):
    return str(sum(list(map(int,list(N)))))

while True:
    N = input()
    if N == "0":
        break
    while True:
        if len(N) == 1:
            print(N)
            break
        N = play(N)