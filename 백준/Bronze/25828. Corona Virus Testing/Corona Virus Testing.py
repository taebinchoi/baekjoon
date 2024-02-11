import math
G, P, T = map(int,input().split())

if G*P < G+P*T:
    print(1)
elif G+P*T < G*P:
    print(2)
else:
    print(0)