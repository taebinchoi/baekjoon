A, B = input().split()

N = int(A.replace('6', '5'))+int(B.replace('6', '5'))
K = int(A.replace('5', '6'))+int(B.replace('5', '6'))

print(N, K)