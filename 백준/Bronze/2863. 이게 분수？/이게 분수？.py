A, B = map(int, input().split()) 
C, D = map(int, input().split()) 
li = [] 
li.append(A/C + B/D) 
li.append(C/D + A/B) 
li.append(D/B + C/A) 
li.append(B/A + D/C) 
ma = max(li) 

print(li.index(ma))