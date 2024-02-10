A = int(input())
B = int(input())

if A >= B:
    print('Congratulations, you are within the speed limit!')
else:
    if 1 <= B-A <= 20:
        print('You are speeding and your fine is $100.')
    elif 21 <= B-A <= 30:
        print('You are speeding and your fine is $270.')
    else:
        print('You are speeding and your fine is $500.')