F = [] 
for i in range(1, 6): 
    N = input() 
    if "FBI" in N: 
        F.append(i) 
if F: 
    print(*F) 
else: 
    print("HE GOT AWAY!")