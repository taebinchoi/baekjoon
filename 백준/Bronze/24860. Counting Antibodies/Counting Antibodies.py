V1, J1 = map(int,input().split())
V2, J2 = map(int,input().split())
V3, D1, J3 = map(int,input().split())

M = V1*J1*V3*D1*J3+V2*J2*V3*D1*J3
print(M)