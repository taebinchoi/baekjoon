for i in range(int(input())):
    n = int(input())
    print(f"Pairs for {n}:",end=' ')
    for j in range(1, n//2+1):
        if j != n-j:
            if j != 1:
                print(',',end=' ')
            print(j, n-j,end='')
    print()