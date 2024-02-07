mo = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

while True:
    c = 0
    sentence = input()
    if sentence == '#':
        break
    for s in sentence:
        if s in mo:
            c += 1
    print(c)