for i in range(3):
    A, B, C, D = map(int, input().split())
    if (A, B, C, D) in ((0, 1, 1, 1), (1, 0, 1, 1), (1, 1, 0, 1), (1, 1, 1, 0)):
        print('A')
    elif (A, B, C, D) in ((0, 0, 1, 1), (0, 1, 0, 1), (0, 1, 1, 0), (1, 0, 0, 1), (1, 0, 1, 0), (1, 1, 0, 0)):
        print('B')
    elif (A, B, C, D) in ((0, 0, 0, 1), (0, 0, 1, 0), (0, 1, 0, 0), (1, 0, 0, 0)):
        print('C')
    elif (A, B, C, D) == (0, 0, 0, 0):
        print('D')
    elif (A, B, C, D) == (1, 1, 1, 1):
        print('E')