while True:
    x, y = map(float, input().split())

    if x == 0 and y == 0:
        print('AXIS')
        break

    if x > 0:
        if y > 0:
            print('Q1')
        elif y < 0:
            print('Q4')
        else:
            print('AXIS')
    elif x < 0:
        if y > 0:
            print('Q2')
        elif y < 0:
            print('Q3')
        else:
            print('AXIS')
    else:
        print('AXIS')
