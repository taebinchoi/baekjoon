M = list(map(int,input().split(':')))
N = list(map(int,input().split(':')))

current = M[0]*3600+M[1]*60+M[2]
salt = N[0]*3600+N[1]*60+N[2]

if current >= salt:
    salt += 24*3600

res = salt - current
A = str(res//3600).zfill(2)
B = str((res%3600)//60).zfill(2)
C = str(res%60).zfill(2)

print('{}:{}:{}'.format(A, B, C))