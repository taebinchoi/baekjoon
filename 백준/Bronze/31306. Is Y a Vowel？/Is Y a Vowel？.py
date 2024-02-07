N = list(input())
M, K = 0, 0
for i in range(len(N)):
    if (N[i] == 'a') or (N[i] == 'e') or (N[i] == 'i') or (N[i] == 'o') or (N[i] == 'u'):
        M += 1 
        K += 1
    if N[i] == 'y':
        K += 1
        
print(M, K)