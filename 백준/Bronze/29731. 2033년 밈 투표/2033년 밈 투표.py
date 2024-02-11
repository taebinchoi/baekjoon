rick_list = [
    'Never gonna give you up', 'Never gonna let you down',
    'Never gonna run around and desert you',
    'Never gonna make you cry', 'Never gonna say goodbye',
    'Never gonna tell a lie and hurt you',
    'Never gonna stop'
]

N = int(input())
in_rick_list = True

for i in range(N):
    value = input()
    if value not in rick_list:
        in_rick_list = False
        break

if in_rick_list:
    print('No')
else:
    print('Yes')
