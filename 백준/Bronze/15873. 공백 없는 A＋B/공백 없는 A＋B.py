N = input()
if len(N) == 4:
    print('20')
elif len(N) == 2:
    print(int(N[0])+int(N[1]))
else:
    if int(N[-1]) == 0:
        print(int(N[0])+10)
    else:
        print(int(N[-1])+10)