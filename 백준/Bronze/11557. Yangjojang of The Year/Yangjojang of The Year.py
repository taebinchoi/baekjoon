T = int(input())
for i in range(T):
    N = int(input())
    school = []
    alc = []
    for i in range(N):
        S, L = input().split()
        school.append(S)
        alc.append(int(L))
    id_ = alc.index(max(alc))
    
    print(school[id_])    