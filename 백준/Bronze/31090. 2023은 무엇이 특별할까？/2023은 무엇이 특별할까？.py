N = int(input())
for i in range(N):
    M = int(input())
    K = M%100
    if (M+1)%K == 0:
        print('Good')
    else:
        print('Bye')