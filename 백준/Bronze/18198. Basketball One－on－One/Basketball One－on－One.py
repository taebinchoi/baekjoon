N = input()
A, B = 0, 0
for i in range(len(N)):
    if N[i] == "A":
        A = A + int(N[i+1])
    elif N[i] == "B":
        B = B + int(N[i+1])
        
print("A" if A>B else "B")