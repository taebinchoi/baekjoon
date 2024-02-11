N = input()
M = list(N)

if "_" in M:
    print(len(M) + 2 +M.count("_")*5)
else:
    print(len(M) + 2)