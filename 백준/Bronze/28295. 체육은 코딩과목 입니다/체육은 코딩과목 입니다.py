move = ["N", "E", "S", "W"]
start = "N"
for i in range(10):
    rot = int(input())
    if rot == 1:
        start = move[(move.index(start) + 1) % 4]
    elif rot == 2:
        start = move[(move.index(start) + 2) % 4]
    elif rot == 3:
        start = move[(move.index(start) + 3) % 4]

print(start)