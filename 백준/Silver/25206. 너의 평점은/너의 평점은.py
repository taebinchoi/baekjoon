Rate = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F']
Grade = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0]
tot = 0
res = 0

for i in range(20):
    M, N, K = input().split()
    N = float(N)
    if K != 'P':
        tot += N
        res += N*Grade[Rate.index(K)]

print('%.6f'%(res/tot)) #소수 여섯째자리까지 출력