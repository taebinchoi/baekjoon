W = float(input())
H = float(input())
B = W/(H*H)

if B > 25:
    print("Overweight")
elif 18.5 < B <= 25:
    print("Normal weight")
else:
    print("Underweight")