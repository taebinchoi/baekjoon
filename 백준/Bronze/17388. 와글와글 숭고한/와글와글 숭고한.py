S, K, H = map(int,input().split())
0 <= S,K,H <= 100
S != K and K != H and S != H

if S+K+H >= 100:
    print('OK')
else:
    if S < K < H or S < H < K:
        print('Soongsil')
    elif K < S < H or K < H < S:
        print('Korea')
    else:
        print('Hanyang')