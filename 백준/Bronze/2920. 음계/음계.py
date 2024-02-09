A, B, C, D, E, F, G, H = map(int,input().split())

if A == 1 and B == 2 and C == 3 and D == 4 and E == 5 and F == 6 and G == 7 and H == 8:
    print("ascending")
elif A == 8 and B == 7 and C == 6 and D == 5 and E == 4 and F == 3 and G == 2 and H == 1:
    print("descending")
else:
    print("mixed")