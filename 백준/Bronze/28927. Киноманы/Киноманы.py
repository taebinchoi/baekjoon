t1, e1, f1 = map(int,input().split())
t2, e2, f2 = map(int,input().split())

if 3*t1+20*e1+120*f1 > 3*t2+20*e2+120*f2:
    print('Max')
elif 3*t1+20*e1+120*f1 < 3*t2+20*e2+120*f2:
    print('Mel')
else:
    print('Draw')