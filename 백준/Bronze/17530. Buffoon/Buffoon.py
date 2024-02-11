N = int(input())
score = []
most = 0

for i in range(N):
    buf = int(input())
    score.append(buf)
    if most < buf:
        most = buf
if most == score[0]:
    print('S')
else:
    print('N')