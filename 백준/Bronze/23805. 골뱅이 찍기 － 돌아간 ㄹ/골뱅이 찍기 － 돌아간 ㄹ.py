def rot(N):
    tot = ['' for i in range(N*5)]
    
    for o in range(N*5):
        if o < N:
            tot[o] = f"{'@'*(N*3)}{' '*N}{'@'*N}"
        elif N <= o < N*4:
            tot[o] = f"{'@'*N}{' '*N}{'@'*N}{' '*N}{'@'*N}"
        else:
            tot[o] = f"{'@'*(N)}{' '*N}{'@'*N*3}"       
    return "\n".join(tot)

if __name__ == "__main__":
    N = int(input())
    print(rot(N=N))