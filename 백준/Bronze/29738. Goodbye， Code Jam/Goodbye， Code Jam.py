def solution(N):
    if N <= 25:
        return 'World Finals'
    elif N <= 1000:
        return 'Round 3'
    elif N <= 4500:
        return 'Round 2'
    else:
        return 'Round 1'
 
if __name__ == '__main__':
    tot = 1
    T = int(input())
    for i in range(T):
        N = int(input())
        result = solution(N)
        print(f'Case #{tot}:',result)
        tot += 1