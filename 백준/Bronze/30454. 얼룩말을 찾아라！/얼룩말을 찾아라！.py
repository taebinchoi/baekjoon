N, L = map(int, input().split())

def count_black_stripes(zebra):
    black_stripes = zebra.split('0')
    return len([grp for grp in black_stripes if grp])

best_zebra = None
max_black_stripes = -1

for _ in range(N):
    zebra = input().strip()
    black_stripes = count_black_stripes(zebra)

    if black_stripes > max_black_stripes:
        max_black_stripes = black_stripes
        best_zebra = 1
    elif black_stripes == max_black_stripes:
        best_zebra += 1

print(max_black_stripes, best_zebra)
