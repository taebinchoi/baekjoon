N = int(input())
if N == 1:
    print("11")
    print("A B C D E F G H J L M")
elif N == 3 or N == 2:
    print("9")
    print("A C E F G H I L M")
elif N == 4:
    print("9")
    print("A B C E F G H L M")
elif N == 5 or N == 6 or N == 7 or N == 8 or N == 9:
    print("8")
    print("A C E F G H L M")
else:
    print("8")
    print("A B C F G H L M")