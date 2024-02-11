A, C, E = map(int,input().split())
AA, CC, EE = map(int,input().split())

if A <= AA and C <= CC and E <= EE:
    print("A")
elif A/2 <= AA and C <= CC and E <= EE:
    print("B")
elif C <= CC and E <= EE:
    print("C")
elif C/2 <= CC and E <= EE:
    print("D")
elif E <= EE:
    print("E")