try:
    while True:
        N = input()
        for i in range(len(N)):
            if N[i] == 'e':
                print("i", end = "")
            elif N[i] == 'i':
                print("e", end = "")
            elif N[i] == 'E':
                print("I", end = "")
            elif N[i] == 'I':
                print("E", end = "")
            else:
                print(N[i], end = "")
        print()
except:
    exit(0)