while True:
    word = input()
    if word == "END":
        break
    else:
        word = word[::-1]
        print(word)