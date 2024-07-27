E, F, C = map(int,input().split())
K = (E+F)//C + (E+F)%C
tot = (E+F)//C
while K//C:
    tot += K//C
    K = K//C + K%C
    
print(tot)