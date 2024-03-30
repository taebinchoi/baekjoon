PI = 3.14159
vol = []
N = int(input())
for i in range(N):
    M = input().split()
    if M[0] == "S":
        vol.append((4/3)*PI*(float(M[1])**3))
    elif M[0] == "C":
        vol.append((1/3)*PI*(float(M[1])**2)*float(M[2]))
    else :
        vol.append(PI*(float(M[1])**2)*float(M[2]))
print("{:.3f}".format(max(vol)))