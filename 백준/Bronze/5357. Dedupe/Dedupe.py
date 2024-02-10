for i in range(int(input())):
    sta = ''
    N = input()
    for j in range(len(N)):
        if sta != N[j]:
            print(N[j], end = "")
            sta = N[j]
    print()