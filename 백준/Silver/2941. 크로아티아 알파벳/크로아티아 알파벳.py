N = input()
croatia = ['c=','c-','dz=','d-','lj','nj','s=','z=']
for i in croatia:
    N = N.replace(i, 'A')
    
print(len(N))