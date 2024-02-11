A = int(input())
B = [int(digit) for digit in str(A)] #A를 리스트로 변환
if B.count(7) == 0:
    if A % 7 == 0:
        print(1)
    else:
        print(0)
else:
    if A % 7 == 0:
        print(3)
    else:
        print(2)