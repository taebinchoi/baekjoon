chess = {"K": 0, "k": 0, "P": 1, "p": 1, "N": 3, "n": 3, "B": 3, "b": 3, "R": 5, "r": 5, "Q": 9, "q": 9}

W, B = 0, 0
for i in range(8):
    piece = input()
    for j in piece:
        if j == ".":
            continue
        if j.isupper():
            W += chess[j]
        else:
            B += chess[j]

print(W-B)