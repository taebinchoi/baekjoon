while 1:
    a, b, c = map(int,input().split())
    if a == b == c == 0:
        break
    if b-a == c-b:
        print("AP", 2*c-b)
    else:
        print("GP", c*c//b)