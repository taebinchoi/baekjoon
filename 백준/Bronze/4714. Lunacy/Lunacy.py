while True:
    N = float(input())
    if N == -1:
        break
    M = ('%.2f'%N)
    K = ('%.2f'%(N*0.167))
    print("Objects weighing "+str(M)+" on Earth will weigh "+str(K)+" on the moon.")