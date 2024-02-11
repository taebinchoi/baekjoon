A = int(input())
B = int(input())
12 >= A >= 1

if A == 1 or 3 or 5 or 7 or 8 or 10 or 12:
    31 >= B >= 1
elif A == 2:
    28 >= B >= 1 
else:
    30 >= B >= 1

if A == 1:
    print("Before")
elif A == 2:
    if 17 >= B >= 1:
        print("Before")
    elif B == 18:
        print("Special")
    else:
        print("After")
else:
    print("After")