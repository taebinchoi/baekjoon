M, S, G = map(float,input().split())
A, B = map(float,input().split())
L, R = map(float,input().split())

lefttime = L/A
righttime = R/B

le = M/G+1 if M % G else M/G
ri = M/S+1 if M % S else M/S

if lefttime+le < righttime+ri:
    print("friskus")
else:
    print("latmask")