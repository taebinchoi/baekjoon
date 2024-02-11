lv, res = input().split()
lv = int(lv)
if res == 'miss':
    print(0)
elif res == 'bad':
    print(lv*200)
elif res == 'cool':
    print(lv*400)
elif res == 'great':
    print(lv*600)
elif res == 'perfect':
    print(lv*1000)