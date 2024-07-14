N = int(input())
S = input()
T = input()
L = len(S)
hamming = 0

for i in range(L):
    if S[i] != T[i]:
        hamming += 1

print(hamming)