import math
import datetime

Y, M, D = input().split('-')
D = int(D)+int(input())
M = int(M)+((D-1)//30)
D = (D-1)%30+1
Y = int(Y)+((M-1)//12)
M = (M-1)%12+1

T1 = datetime.datetime(Y, M, D)
print(T1.strftime('%Y-%m-%d'))