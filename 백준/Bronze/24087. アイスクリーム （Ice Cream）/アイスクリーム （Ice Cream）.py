S = int(input())
A = int(input())
B = int(input())

if S <= A:
    print(250)
else:
    if (S-A)//B == ((S-A)/B):
        print(250+((S-A)//B)*100)
    else:
        print(250+((S-A)//B+1)*100)