N = int(input())

for i in range(N):
    A, B, C, D = map(int,input().split())
    tot = B + C + D
    if tot < 55:
        res = f"{A} {tot} FAIL"
        print(res)
    elif B/35 < 0.3:
        res = f"{A} {tot} FAIL"
        print(res)
    elif C/25 < 0.3:
        res = f"{A} {tot} FAIL"
        print(res)
    elif D/40 < 0.3:
        res = f"{A} {tot} FAIL"
        print(res)
    elif D/40 >= 0.3 and C/25 >= 0.3 and B/35 >= 0.3:
        res = f"{A} {tot} PASS"
        print(res)