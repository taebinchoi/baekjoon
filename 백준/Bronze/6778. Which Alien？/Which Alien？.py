N = int(input())
A = int(input())

if N >= 3 and A <= 4:
    print("TroyMartian")
if N <= 6 and A >= 2:
    print("VladSaturnian")
if N <= 2 and A <= 3:
    print("GraemeMercurian")