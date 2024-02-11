t1, m1, t2, m2 = map(int,input().split())

if 60*t1+m1 <= 60*t2+m2:
    M = (60*t2+m2) - (60*t1+m1)
    N = M//30
else:
    M = (60*(t2+24)+m2) - (60*t1+m1)
    N = M//30

print(M, N)