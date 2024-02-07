while 1:
    N = input()
    if N == '0':
        break
    fin = len(N)+1
    for i in N:
        if i == '0':
            fin += 4 
        elif i == '1':
            fin += 2
        else:
            fin += 3
    print(fin)