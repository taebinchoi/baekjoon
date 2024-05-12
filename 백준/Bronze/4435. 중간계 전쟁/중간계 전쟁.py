N = int(input())

for i in range(1, N+1):
    G = list(map(int,input().split()))
    S = list(map(int,input().split()))

    Gscore = G[0] + G[1]*2 + G[2]*3 + G[3]*3 + G[4]*4 + G[5]*10
    Sscore = S[0] + S[1]*2 + S[2]*2 + S[3]*2 + S[4]*3 + S[5]*5 + S[6]*10

    if Gscore > Sscore:
        print(f"Battle {i}: Good triumphs over Evil")
    elif Gscore < Sscore:
        print(f"Battle {i}: Evil eradicates all trace of Good")
    else:
        print(f"Battle {i}: No victor on this battle field")