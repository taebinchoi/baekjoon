H1, M1, S1 = map(int,input().split(':'))
H2, M2, S2 = map(int,input().split(':')) # : caution!

T1 = H1*3600 + M1*60 + S1
T2 = H2*3600 + M2*60 + S2
if T1 > T2:
    print(T2-T1+3600*24)
else:
    print(T2-T1)